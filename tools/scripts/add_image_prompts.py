import os, re

BASE = '/Users/suman/Desktop/ByteXL/content/Semester 1'

STYLE = (
"STYLE: world-class high-end 3D RENDER, cinematic and vibrant, the quality of a top animation studio or an "
"award-winning CGI key visual. Glossy, soft 3D forms with physically based materials, global illumination, soft "
"contact shadows, gentle ambient occlusion, subtle reflections, rim light and bloom, and a shallow depth of field. "
"Dynamic three-quarter hero camera angle with real depth, scale, and a sense of motion. Premium, playful, and "
"polished. Explicitly NOT a flat vector diagram and NOT a textbook illustration. Use a vivid green accent for "
"positive or yes outcomes and a vivid red accent for negative or no outcomes, on a soft studio-gradient backdrop "
"with a glowing focal element. Ultra-detailed, 4k, crisp."
)

CHAR = {
"Unit 2 - Data Types and Operators":
 "CHARACTER & THEME: no single recurring host for this unit. Each lesson below names its own ordinary, relatable "
 "Indian person and everyday setting (a librarian, a pharmacist, a tailor, an electrician, a gardener, a mechanic, "
 "a security guard, a cashier, a teacher, a receptionist) — use exactly that person and setting for that lesson, "
 "and do not reuse the same character, outfit, or location in any other lesson of this unit. Render each one as a "
 "warm, appealing stylized 3D animated person in the polished style of a modern Pixar or DreamWorks film, dressed "
 "and equipped appropriately for their own scene, with a colour palette that suits that specific scene rather than "
 "one fixed unit-wide palette. Data types and operators appear as real objects from that scene's setting, never as "
 "generic glowing boxes.",
"Unit 3 - Control Flow":
 "CHARACTER & THEME (keep identical across every lesson of THIS unit, distinct from other units): Asha, a confident, "
 "friendly stylized 3D animated hero in the polished style of a modern Pixar or DreamWorks film: a cheerful young "
 "Indian college student in her late teens, shoulder-length dark hair, wearing a teal hoodie and dark jeans, almost "
 "always with her smartphone in hand. This whole unit follows Asha through ordinary student daily life, where small "
 "yes-or-no decisions decide what happens next: unlocking her phone, a low-battery warning, checking exam marks on "
 "the college app, opening a streaming app, picking from a canteen menu, filling an online signup form. Cool blue "
 "base palette with a warm phone-screen glow. Keep Asha's design and the palette consistent in every image of this "
 "unit, and ground every scene in a real, relatable student moment (a phone screen, an app, a form) rather than an "
 "invented mechanism.",
"Unit 4 - Looping":
 "CHARACTER & THEME (keep identical across every lesson of THIS unit, distinct from other units): Kabir, a warm, "
 "energetic stylized 3D animated hero in the polished style of a modern Pixar or DreamWorks film: a friendly young "
 "Indian college student around twenty, short neat dark hair, a confident grin, wearing a mustard-and-orange hoodie "
 "over a tee and jeans, usually holding his smartphone or a class clipboard as the busy class representative. This "
 "whole unit follows Kabir through ordinary student life whenever the same task must be repeated many times: "
 "messaging every classmate, retrying a wifi password, counting gym reps, scrolling a feed, arranging an Instagram "
 "photo grid, tallying class results, a song stuck on repeat. Warm orange-and-amber base palette with a soft "
 "phone-screen glow. Keep Kabir's design and the palette consistent in every image of this unit, and ground every "
 "scene in a real, relatable student moment of repetition rather than a factory or machine.",
"Unit 5 - Strings":
 "CHARACTER & THEME (keep identical across every lesson of THIS unit, distinct from other units): Meera, a warm, "
 "creative stylized 3D animated hero in the polished style of a modern Pixar or DreamWorks film: a friendly young "
 "Indian college student around nineteen, round glasses, dark hair in a loose braid, wearing a denim jacket over a "
 "printed tee, almost always editing something on her phone or laptop. She runs a small handmade-craft Instagram "
 "page, so this whole unit follows her through ordinary student life spent handling TEXT: typing usernames and "
 "captions, fixing typos in messages, splitting hashtags, searching chats, formatting a price list, writing a "
 "multi-line bio. Cosy purple-and-teal base palette with a soft phone-screen glow. Keep Meera's design and the "
 "palette consistent in every image of this unit, and ground every scene in a real, relatable student moment with "
 "text on a phone or laptop rather than an archaic or invented mechanism.",
}

def block(img, char_theme, title, scene, labels):
    return (
"<!--\n"
f"IMAGE PROMPT  ->  generate as {img}   (16:9 cinematic hero image, place here, right after the Introduction)\n\n"
f"{char_theme}\n\n"
f"{STYLE}\n\n"
f"SCENE: {scene}\n\n"
f"ON-IMAGE TEXT: show a short bold title \"{title}\" as a clean headline, plus only these few labels, large and "
f"legible: {labels}. Keep text tasteful and minimal - a headline and a handful of labels, never sentences or paragraphs.\n\n"
"GOAL: a striking, world-class 3D hero image that makes the idea instantly clear and exciting; rich depth and "
"lighting, minimal but appealing text, no clutter.\n"
"-->"
    )

# prefix -> (title, scene, labels, fallback_basename, alt)
DATA = {
"Unit 2 - Data Types and Operators": {
 "01": ("Labels for your data", "A librarian at the stacks, using a handheld label-gun to print and stick a crisp tag onto a book's spine, then sliding the book onto the shelf that now bears that exact label, a glowing title value settling into place right after labelling it.", "name | age | city | =", "01_variables_assignment_naming.png", "Variables as labelled books holding values"),
 "02": ("Three kinds of numbers", "A pharmacist at the counter: whole tablets counted out onto one tray, cough syrup poured into a beaker marked precisely to a decimal line beside it, and a fizzy antacid glass swirling with two layered colours of bubbles past it.", "int | float | complex", "02_numbers_int_float_complex.png", "Python number types as pharmacy measures"),
 "03": ("Text and True or False", "A tailor at the cutting table, chalking a customer's name in flowing cursive across a garment, while an order tag pinned beside it flips between a green check and a red cross for whether the order is ready.", "string = text | True | False", "03_strings_booleans.png", "Strings hold text, booleans hold True or False"),
 "04": ("Change the type", "An electrician at a workbench, feeding a wire wearing a tag that reads the text \"20\" into a multimeter, pressing a button, and the digital display lighting up with the solid number 20.", "\"20\" | 20 | int()", "04_type_conversion_casting.png", "Type conversion turns text into a number"),
 "05": ("Doing the maths", "A gardener seen from above, dividing a tray of seedlings into equal rows for planting along a bed, with one small leftover seedling set neatly to one side as a remainder.", "+  -  *  / | // | %", "05_arithmetic_operators.png", "Arithmetic, equal rows and a remainder"),
 "06": ("Ask a question", "A mechanic in the garage, placing two tyres on an old brass two-pan balance scale, the heavier pan dipping down and lighting a glowing indicator green for true or red for false above it.", ">  <  == | True | False", "06_comparison_operators.png", "Comparison operators return True or False"),
 "07": ("Combine conditions", "A security guard at a building entrance, where two separate keycard readers wired as switches must both flash green together before the turnstile gate unlocks.", "AND | OR | NOT", "07_logical_operators.png", "Logical operators combine conditions"),
 "08": ("Update in place", "A cashier at the billing counter beside a tall glass jar labelled total that already holds a stack of coins, dropping in one more coin so the level inside rises visibly higher than before.", "total | += 50", "08_augmented_assignment.png", "Augmented assignment grows a running total"),
 "09": ("Who goes first?", "A teacher pinning a worksheet to the classroom board, circling question 2, multiply first, with a do this first marker, ahead of question 3, add the total, while a small parentheses-shaped clip holds that circled step at the very front of the sheet.", "() | 2 + 3 * 4 = 14", "09_operator_precedence.png", "Operator precedence decides what runs first"),
 "10": ("Talk to the user", "A receptionist leaning through the front desk window, taking a handwritten request slip fluttering in from a visitor, and sliding back a printed visitor badge with the visitor's name filled in.", "input -> | -> print | f-string", "10_input_output_fstrings.png", "input, print and f-strings in a conversation"),
},
# Unit 3 - Control Flow: image prompts intentionally removed (lessons use no images).
"Unit 4 - Looping": {
 "01": ("Let the loop do it", "Split scene: on the left a tired Kabir thumb-typing the same college-fest reminder to classmates one by one on his phone, dozens of identical chat bubbles stacking up and his thumb aching; on the right a relaxed Kabir tapping once as a loop fires the very same message to all sixty classmates at once.", "one by one | with a loop", "01_why_loops_by_hand_vs_loop.png", "Loops replace sending the same message one by one"),
 "02": ("Repeat until done", "Kabir sitting on his hostel bed trying the wifi password again and again on his phone, each wrong attempt flashing red, his eyes fixed on the little wifi icon, ready to stop the instant it finally turns green and connects, with no idea how many tries it will take.", "while wrong: try again | connected", "02_while_until_correct.png", "A while loop retries until the wifi connects"),
 "03": ("Step through a range", "Kabir at the hostel gym counting out a fixed set of reps, glowing numbers 0 1 2 3 4 floating above him one per push-up, knowing the exact count before he starts and stopping cleanly the moment he hits the last one.", "range(5) | 0 1 2 3 4", "03_for_range_stepping_stones.png", "A for loop steps through a known count of reps"),
 "04": ("Visit each item", "Kabir scrolling the class WhatsApp group member list on his phone, a highlight moving down each name in turn, Aisha then Ravi then Meera, one at a time, while beside it the letters of a fest hashtag light up one by one too.", "for each name", "04_iterating_letters.png", "Iterating over each item in a list, one at a time"),
 "05": ("Stop or skip", "Kabir scrolling his social feed on his phone to find one specific post: he slaps a glowing STOP the instant he spots the one he wanted (break), while earlier flicking quickly past sponsored ad posts without stopping (continue).", "break = stop | continue = skip", "05_break_continue.png", "break stops scrolling at a match, continue skips a post"),
 "06": ("Rows and columns", "Kabir arranging his Instagram profile photo grid on his phone, filling it row by row and within each row placing each photo square one at a time, an outer pass for the rows and an inner pass for the columns.", "rows x columns", "06_nested_loops_grid.png", "Nested loops fill a photo grid row by row"),
 "07": ("The loop toolkit", "Kabir at his laptop tallying the class-fest results, four quick jobs at once glowing around him: counting how many classmates joined, summing the money collected, finding the top scorer, and searching the list for one name.", "count | sum | max | search", "07_loop_patterns_toolkit.png", "Common loop patterns: count, sum, max, search"),
 "08": ("Two classic bugs", "Split scene: on one side, Kabir's favourite song stuck on repeat forever on his phone, the loop arrow spinning endlessly and never moving on; on the other side, Kabir counting chairs for an event and ending up exactly one short, an off-by-one slip at the very last seat.", "infinite! | off by one", "08_infinite_and_off_by_one.png", "A song stuck on repeat, and a count that is off by one"),
},
"Unit 5 - Strings": {
 "01": ("Text is a sequence", "Meera on her phone typing a new username for her craft page, each letter appearing one at a time in the box with a live character-count ticking up beside it, showing that a name is just an ordered run of characters.", "m e e r a | len = 5", "01_string_beads.png", "A username is an ordered sequence of characters"),
 "02": ("Reach in and slice", "Meera on her phone pulling pieces out of text: tapping to grab just the first letter of a friend's name for an initial, then selecting only the last four digits of a long phone number, without retyping anything.", "first letter | last 4 | [1:4]", "02_indexing_slicing_beads.png", "Indexing one character and slicing a run of characters"),
 "03": ("Build, do not edit", "Meera spotting a typo in a username she has already locked in, tapping the single wrong letter but finding she cannot change just that one character, so she clears it and types a fresh corrected username instead, shown beside the unchanged original.", "cannot edit one letter | type new", "03_immutability_locked.png", "You cannot edit one character, so you build a new string"),
 "04": ("Transform your text", "Meera tidying a messy caption on her phone: one tap turns it into neat capitals, another trims the stray spaces at the ends, another swaps an old shop name for the new one, each tap producing a fresh clean version.", "upper | strip | replace", "04_string_methods_toolbox.png", "String methods clean and transform a caption"),
 "05": ("Split and join", "Meera on her phone breaking a single line of hashtags reading handmade,gifts,pune apart at each comma into separate tags, then joining a set of loose words back together into one neat hashtag.", "split -> | <- join", "05_split_join.png", "split breaks text apart at commas, join combines it"),
 "06": ("Find it in text", "Meera on her phone checking a customer's email she just typed for the @ sign, the app flagging one entry reading asha gmail.com that is missing it, while she also searches a caption for a word and counts how often a hashtag appears.", "in? | find | count", "06_searching_magnifier.png", "Searching text: does it contain, where, how many times"),
 "07": ("Make it look neat", "Meera on her phone formatting a price list for her handmade-shop post so it looks tidy, item names lined up on the left and prices in a neat column on the right, every price rounded to two decimals.", ".2f | aligned columns", "07_formatting_aligned_table.png", "Formatting prices into neat aligned columns"),
 "08": ("Shape the layout", "Meera writing a multi-line Instagram bio on her phone, dropping the greeting onto its own line and indenting the next line, and tucking a quoted phrase inside the text with its quote marks intact.", "\\n new line | \\t tab", "08_escape_multiline.png", "Line breaks and tabs shape a multi-line caption"),
 "09": ("Clean, parse, analyze", "Meera at her laptop cleaning up a messy batch of giveaway entry messages full of stray spaces and odd capitals, trimming and lowering each, splitting them into pieces, while a tidy count of words and entries builds beside her.", "clean -> parse -> analyze", "09_text_processing_analyst.png", "Cleaning and analysing a batch of messy entries end to end"),
},
}

img_re = re.compile(r'^!\[.*\]\(.*\)\s*$', re.M)
strip_re = re.compile(r'<!--.*?IMAGE PROMPT.*?-->\n*', re.S)

changed = []
for unit, files in DATA.items():
    folder = os.path.join(BASE, unit)
    char_theme = CHAR[unit]
    for fn in sorted(os.listdir(folder)):
        if not re.match(r'\d{2}_.*\.md$', fn):
            continue
        prefix = fn[:2]
        if prefix not in files:
            continue
        title, scene, labels, basename, alt = files[prefix]
        path = os.path.join(folder, fn)
        content = open(path, encoding='utf-8').read()
        content = strip_re.sub('', content)
        m = img_re.search(content)
        if m:
            img = re.search(r'\((images/[^)]+)\)', content[m.start():]).group(1)
            blk = block(img, char_theme, title, scene, labels)
            content = content[:m.start()] + blk + '\n\n' + content[m.start():]
        else:
            blk = block('images/' + basename, char_theme, title, scene, labels)
            idx = content.index('## Introduction')
            nxt = content.find('\n## ', idx + 5)
            ins = '\n' + blk + '\n\n' + f'![{alt}](images/{basename})\n'
            content = content[:nxt] + ins + content[nxt:]
        open(path, 'w', encoding='utf-8').write(content)
        changed.append(f"{unit}/{fn}")

print("files updated:", len(changed))
