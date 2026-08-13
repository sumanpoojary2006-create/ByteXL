## Introduction

A state transport corporation adds a voice line so passengers can check bus timings by phone instead of navigating a menu. It works well in testing and poorly in service, and the failure log is instructive.

It mishears place names constantly, because the announcer who recorded the test data pronounced them carefully and callers do not. It fails on callers who switch between English and the local language within one sentence, which is how most people actually speak. It fails at bus stands, where the ambient noise is a wall of engines and voices. And it struggles with older callers, whose speech is slower and whose vocabulary differs from the young urban speakers in the training data.

None of these is a failure to understand language. The system never got as far as language. It failed at the earlier problem of turning a pressure wave into words at all.

That problem, in both directions, is **speech AI**.

**Definition:** `Speech AI` covers `speech recognition`, which converts an audio signal into text, and `speech synthesis`, which converts text into audible speech, together forming the voice interface that sits in front of any language system.

![Visual explanation of introduction](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/03_section_introduction.png)

## What Makes Speech Different From Text

It is tempting to treat speech as text with an extra step, and the differences are large enough to make that misleading.

**There are no spaces.** Written words are separated for you. Speech is continuous, and where one word ends and the next begins is something the listener infers. "Ice cream" and "I scream" can be acoustically near-identical, and the same is true across every language.

**The same word is never said the same way twice.** Pitch, pace, accent, emphasis, and the acoustics of the room all change the signal while leaving the word unchanged. This is the invariance problem again, in a new medium.

**The signal is enormous and mostly redundant.** A second of speech at typical quality is sixteen thousand numbers, carrying perhaps two or three words. Almost all of it is detail the meaning does not depend on.

**It arrives over time and cannot be re-read.** A reader can glance back at a sentence. A live recogniser must commit, and if it needs a later word to disambiguate an earlier one, it has to be able to revise.

**Noise is not separable.** In text, a typo is localised. In audio, a passing bus is mixed into the same signal as the voice, occupying the same frequencies, and cannot be simply removed.

![Visual explanation of what makes speech different from text](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/03_section_what_makes_speech_different_from_text.png)

## How Recognition Works

The pipeline has three stages, and the modern version has collapsed the middle ones.

**Acoustic processing** converts the raw waveform into a compact representation. The signal is chopped into short overlapping windows of perhaps 25 milliseconds, and each is described by how much energy sits at each frequency. The result is a picture of how the sound's frequency content changes over time, which is small enough to model and retains what matters for distinguishing speech sounds.

**Acoustic modelling** maps those frequency patterns onto units of sound. Older systems predicted phonemes, the individual sounds a language distinguishes; modern ones often predict characters or sub-word pieces directly.

**Language modelling** decides which sequence of words is plausible. This is the stage that resolves "ice cream" against "I scream", not from the audio, which is ambiguous, but from which is more likely in context. Speech recognition has always depended on a language model doing a substantial part of the work, and this is why systems improve when they know the topic.

The historically important shift was from separate hand-engineered components to one network trained end to end on audio paired with transcripts. The pieces above still describe what happens; they are simply no longer separate systems built by separate teams.

![Visual explanation of speech recognition pipeline](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/03_speech_recognition_pipeline_context_v4.png)

## Why the Transport Line Failed

Each failure in the log maps onto a known difficulty, and naming them is more useful than treating them as bad luck.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Observed failure</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Underlying cause</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Usual remedy</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Mishears place names</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Rare words the language model has barely seen</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Bias the recogniser towards a known list of stop names</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Fails on mixed-language sentences</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Trained on one language at a time</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Train on code-switched speech, which is scarce</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Fails in noisy places</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Training audio was clean</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Add noise to training data deliberately</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Struggles with older callers</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Under-representation in the training set</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Collect speech from the actual user population</td>
    </tr>
  </tbody>
</table>

The third row deserves a note, because the remedy is counter-intuitive and standard. Rather than trying to clean the incoming audio, systems are trained on deliberately degraded versions of clean recordings, with traffic noise, room echo, and telephone distortion mixed in. Making the training data worse makes the deployed system better, which is a general technique called augmentation.

The fourth row is the same representation problem that appears in vision, and it has the same character: nobody excluded older speakers, they were simply not in the data that was convenient to collect.

![Visual explanation of why the transport line failed](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/03_section_why_the_transport_line_failed.png)

## Measuring Recognition

The standard measure is `word error rate`: the number of words wrongly inserted, deleted, or substituted, divided by the number of words actually spoken.

Two properties are worth knowing. It can exceed 100 percent, since a system can insert more words than were said. And it treats all errors alike, which is often wrong: mishearing "the" costs nothing, and mishearing a bus stand name makes the whole call useless.

A figure quoted without conditions is close to meaningless. The same system may report 5 percent on clean read speech and 30 percent on a call from a bus stand. **When a vendor quotes a word error rate, the question to ask is what audio it was measured on**, and whether that audio resembles what the system will actually hear.

![Visual explanation of measuring recognition](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/03_section_measuring_recognition_simple_v2.png)

## Speech Synthesis

Going the other way has a different shape of difficulty. Producing intelligible speech from text has been possible for decades; producing speech that does not sound wrong is harder.

Three problems account for most of it.

**Deciding how to say what is written.** Text underspecifies pronunciation. "2/3" might be a fraction, a date, or a ratio. A number could be a quantity or a phone number. Names carry pronunciations no rule predicts. This normalisation step is unglamorous and is where a great many synthesis errors originate.

**Prosody.** The rhythm, stress, and intonation carrying meaning beyond the words. The difference between a statement and a question is often entirely prosodic, and flat prosody is what made older synthetic voices sound robotic even when every phoneme was correct.

**Naturalness.** Modern systems generate the waveform directly with neural models and are close to indistinguishable from a recording, which is a genuine achievement and creates the obvious problem: a synthesised voice can convincingly imitate a specific person from a small sample, which is now a routine mechanism for fraud.

![Visual explanation of speech synthesis](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/03_section_speech_synthesis.png)

## What a Voice Assistant Actually Contains

A single spoken request passes through more stages than the interface suggests.

1. **Wake word detection** runs continuously on the device, using a small model listening for one phrase. This is why it can respond without streaming everything you say, and it is also why the device is always listening in a literal sense.
2. **Speech recognition** converts the request to text.
3. **Intent understanding** decides what was wanted and extracts the details, such as the destination and the time.
4. **Action** queries a timetable, sets an alarm, or calls another system.
5. **Response generation** produces the text of the reply.
6. **Speech synthesis** speaks it.

Only stages 2 and 6 are speech AI. The rest is language understanding and ordinary software, which is worth remembering when a voice assistant fails: the failure is often not in hearing you.

The privacy question sits at stage 1 and is genuinely a design decision. Running wake word detection on the device means audio is only transmitted after the phrase is heard. Whether recognition itself happens on the device or in a data centre is a trade between capability and what leaves the room, and different products answer it differently.

![Visual explanation of voice assistant stack](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/03_voice_assistant_stack.png)

## Your Turn

Redesign the transport corporation's data collection.

The original test recordings were made by an announcer in a quiet room. Write a specification for the audio that should have been collected instead, covering who speaks, where they are, and what they say. Be specific enough that somebody could execute it. Then estimate how many recordings you would need for a system covering two hundred bus stands, and consider whether that is achievable.

Then think about the error measure. Word error rate counts every word equally. Design a better measure for this specific application, where getting the bus stand name right is everything and getting "please" right is nothing. Then say why, despite your measure being more appropriate, word error rate is still the number everyone reports.

Finally, take the augmentation idea and push on it. Adding traffic noise to clean recordings makes the system robust to traffic noise. Name two ways this could fail: something about real bus-stand audio that mixing in a noise recording would not reproduce. If your answer involves people speaking over each other, or the way a speaker raises their voice and changes their pronunciation in a loud place, you have identified the limits of augmentation and why collecting real data in real conditions remains necessary.
