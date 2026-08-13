## Introduction

A quality inspector at a textile mill near Tiruppur can glance at a moving length of fabric and spot a flaw in under a second. She has been doing it for nineteen years. The mill wants a camera to do the same thing, and the request sounds modest, because she makes it look effortless.

It is not effortless; it is invisible. What reaches her eyes is a pattern of light, and everything else, the sense that there is fabric rather than a coloured field, that a slightly darker streak is a pulled thread rather than a shadow, that this particular irregularity is a defect while that one is the weave, happens below the level she can report on. Asked how she does it, she says she just sees it.

A camera produces the same pattern of light as a grid of numbers, perhaps two million of them, and nothing else. Every part of what the inspector adds has to be reconstructed.

Building systems that extract meaning from images is **computer vision**, and its difficulty is precisely that it automates something humans do without noticing they are doing it.

**Definition:** `Computer vision` is the field concerned with extracting meaning from images and video, spanning tasks from assigning a single label to a picture, through locating objects within it, to labelling every individual pixel.

![Visual explanation of introduction](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/02_section_introduction_simple_v2.png)

## Why Pixels Are Hard

An image is a grid of brightness values, three per pixel for colour. That representation is complete, in the sense that nothing about the picture is missing from it, and it is almost useless, because the thing you want to know is not written anywhere in it.

Four specific difficulties explain why this took decades.

1. **Nothing marks an object.** There is no boundary in the numbers saying where the fabric ends and the machine begins. Boundaries are inferred from changes in brightness, and many real boundaries produce no change while many changes are not boundaries.

2. **The same object produces wildly different numbers.** Move the light, and every value changes. Rotate the fabric, and the grid is unrecognisable as an array while being obviously the same to a person. This is the invariance problem, and it is the central one.

3. **Different objects produce similar numbers.** A shadow and a dark stain can be numerically identical in a region while meaning entirely different things.

4. **The dimensions are enormous.** Two million numbers per image means any method that treats each independently needs an impossible quantity of data.

The inspector solves all four continuously and cannot describe how, which is exactly the situation where hand-written rules fail and learning from examples succeeds.

![Visual explanation of why pixels are hard](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/02_section_why_pixels_are_hard.png)

## Three Tasks, Increasing in Difficulty

"Computer vision" covers several tasks that are routinely confused, and the distinction matters because they need different data, different outputs, and different amounts of labelling effort.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Task</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Question answered</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Output</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Cost of labelling one example</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Image classification</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">What is this a picture of?</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">One label for the whole image</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Seconds; pick from a list</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Object detection</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">What is in it, and where?</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A box and a label per object</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A minute; draw every box</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Semantic segmentation</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Which category does each pixel belong to?</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A label for every pixel</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Many minutes; trace every outline</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Instance segmentation</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Which pixels belong to which individual object?</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A separate outline per object</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Longest; trace each object separately</td>
    </tr>
  </tbody>
</table>

Read the last column, because it drives project decisions more than the accuracy figures do. Classification labels can be gathered cheaply and in bulk. Segmentation labels require somebody to trace outlines by hand, so a dataset of ten thousand segmented images represents an enormous quantity of human work, and that cost is usually what determines which task a project can afford.

The distinction between the last two rows is the one people miss. Semantic segmentation marks every pixel that is "person"; instance segmentation distinguishes the third person from the fourth. For counting objects in a crowded scene, only the second will do.

![Visual explanation of vision tasks](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/02_vision_tasks.png)

## What the Mill Actually Needs

Applying this to the fabric inspection makes the choice concrete.

Classification would answer "does this frame contain a defect", which is enough to stop the line and no help in finding the flaw. Detection would put a box around it, which lets an operator go straight to the spot. Segmentation would trace the flaw's exact shape, which matters if the mill wants to measure it and classify the fault type by its geometry.

Each step up costs more to label and more to run. **The right task is the least demanding one that answers the question the business is actually asking**, and starting at segmentation because it sounds most thorough is a common and expensive error.

![Visual explanation of what the mill actually needs](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/02_section_what_the_mill_actually_needs.png)

## Three Deployed Systems

The blueprint for this course names three case studies, and each illustrates a different practical concern.

**Face unlock** is a verification problem rather than a recognition one, and the distinction matters. The phone is not asking who this is among all people; it is asking whether this is the one enrolled face. That is a far easier question, which is why it works reliably on modest hardware. The genuine engineering difficulty is not accuracy but resisting a photograph of the owner, which is why devices project infrared dots to check the face has depth. Note also that everything happens on the device: the face data never leaves it, which is a deliberate design choice about privacy rather than a technical necessity.

**Medical imaging** is where the evaluation lessons from earlier in this course bite hardest. A model that flags possible findings on a scan operates on a rare-class problem with two very different kinds of error, so accuracy is meaningless and the threshold is a clinical decision rather than a technical one. The deployed systems are almost all assistive: they mark regions for a radiologist to examine rather than issuing a verdict, partly for liability and partly because a second reader who never tires is genuinely useful even when imperfect.

**Autonomous driving** is the hardest of the three because it is real-time, safety-critical, and open-ended. It needs detection and segmentation simultaneously, at many frames a second, in rain and glare and at night, and it must handle situations nobody anticipated. It is also the clearest illustration that perception is not the whole problem: knowing there is a cyclist ahead is a small part of deciding what to do about them.

![Visual explanation of vision deployment failures](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/02_vision_deployment_failures.png)

## What Vision Systems Still Get Wrong

An honest account has to include the failures, because they are systematic rather than random.

**Distribution shift.** A model trained on daytime footage from one city degrades on night footage from another. The mill's inspector adapts instantly to a new fabric; a model trained on cotton may be useless on denim.

**Spurious correlations.** A model asked to detect a disease from chest scans may learn to recognise which hospital took the image, from a marker in the corner, if one hospital happened to see sicker patients. It scores well in testing and fails in deployment, and the failure is invisible until someone checks what the model is looking at.

**Adversarial fragility.** Small, carefully chosen changes to an image, often imperceptible to a person, can flip a confident classification entirely. This is not a bug in a particular model but a general property of the way these systems draw boundaries.

**Uneven performance across groups.** Face systems have been repeatedly shown to perform worse on darker skin tones and on women, tracing directly to training sets in which those groups were under-represented. This is the representation bias problem in its most documented form.

The common thread is worth stating. **These systems learn what reliably distinguishes their training examples, which is not always what a person would consider the actual subject.** The hospital marker and the disease are equally good predictors within the training data, and nothing in the training objective prefers the right one.

![Visual explanation of what vision systems still get wrong](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/02_section_what_vision_systems_still_get_wrong.png)

## Your Turn

Specify the vision system for the mill properly, without writing any code.

Decide which of the four tasks the mill should build first, and justify it by what the operator will do with the output rather than by which is most capable. Then estimate the labelling cost: if a defect appears in roughly one frame in two hundred and you want a thousand labelled defects, how many frames must somebody look at? That number, rather than the model architecture, is usually what decides whether such a project happens.

Then design a test for the spurious correlation problem. Suppose the mill's defective samples were all photographed on the morning shift and the good ones on the afternoon shift, when the lighting differs. Describe what the model would probably learn, what its test accuracy would look like, and one concrete check you could run on the trained model to detect the problem before deployment.

Finally, take the distribution shift seriously. List four ways the images reaching the deployed camera will differ from the images used for training, thinking about the physical realities of a working mill rather than about photography. Then say, for each, whether you would fix it by collecting more varied training data or by controlling the environment. Both are legitimate engineering answers, and choosing between them is the real decision.
