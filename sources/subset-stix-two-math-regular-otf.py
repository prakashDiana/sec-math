#!/usr/bin/python
# coding=UTF-8
#
# Copyright 2016 Google Inc. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Create a curated subset."""

import sys

from nototools import subset
from nototools import unicode_data

# default emoji characters in the BMP, based on
# http://www.unicode.org/draft/Public/emoji/1.0/emoji-data.txt
# (partial, others needed for STIX)
BMP_DEFAULT_EMOJI = {
    0x231B, # ⌛ HOURGLASS
    0x23E9, # ⏩ BLACK RIGHT-POINTING DOUBLE TRIANGLE
    0x23EA, # ⏪ BLACK LEFT-POINTING DOUBLE TRIANGLE
    0x23EB, # ⏫ BLACK UP-POINTING DOUBLE TRIANGLE
    0x23EC, # ⏬ BLACK DOWN-POINTING DOUBLE TRIANGLE
    0x23F0, # ⏰ ALARM CLOCK
    0x23F3, # ⏳ HOURGLASS WITH FLOWING SAND
    0x2614, # ☔ UMBRELLA WITH RAIN DROPS
    0x2615, # ☕ HOT BEVERAGE
    0x264A, # ♊ GEMINI
    0x264B, # ♋ CANCER
    0x264C, # ♌ LEO
    0x264D, # ♍ VIRGO
    0x264E, # ♎ LIBRA
    0x264F, # ♏ SCORPIUS
    0x2650, # ♐ SAGITTARIUS
    0x2651, # ♑ CAPRICORN
    0x2652, # ♒ AQUARIUS
    0x2653, # ♓ PISCES
    0x267F, # ♿ WHEELCHAIR SYMBOL
    0x2693, # ⚓ ANCHOR
    0x26A1, # ⚡ HIGH VOLTAGE SIGN
    0x26BD, # ⚽ SOCCER BALL
    0x26BE, # ⚾ BASEBALL
    0x26C4, # ⛄ SNOWMAN WITHOUT SNOW
    0x26C5, # ⛅ SUN BEHIND CLOUD
    0x26CE, # ⛎ OPHIUCHUS
    0x26D4, # ⛔ NO ENTRY
    0x26EA, # ⛪ CHURCH
    0x26F2, # ⛲ FOUNTAIN
    0x26F3, # ⛳ FLAG IN HOLE
    0x26F5, # ⛵ SAILBOAT
    0x26FA, # ⛺ TENT
    0x26FD, # ⛽ FUEL PUMP
    0x2705, # ✅ WHITE HEAVY CHECK MARK
    0x270A, # ✊ RAISED FIST
    0x270B, # ✋ RAISED HAND
    0x2728, # ✨ SPARKLES
    0x274C, # ❌ CROSS MARK
    0x274E, # ❎ NEGATIVE SQUARED CROSS MARK
    0x2753, # ❓ BLACK QUESTION MARK ORNAMENT
    0x2754, # ❔ WHITE QUESTION MARK ORNAMENT
    0x2755, # ❕ WHITE EXCLAMATION MARK ORNAMENT
    0x2757, # ❗ HEAVY EXCLAMATION MARK SYMBOL
    0x2795, # ➕ HEAVY PLUS SIGN
    0x2796, # ➖ HEAVY MINUS SIGN
    0x2797, # ➗ HEAVY DIVISION SIGN
    0x27B0, # ➰ CURLY LOOP
    0x27BF, # ➿ DOUBLE CURLY LOOP
    0x2B55, # ⭕ HEAVY LARGE CIRCLE
}

def main(argv):
    """Subset a font.

    The first argument is the source file name, and the second argument is
    the target file name.
    """

    source_file_name = argv[1]
    target_file_name = argv[2]
    subset.subset_font(
        source_file_name,
        target_file_name,
        exclude=BMP_DEFAULT_EMOJI)


if __name__ == '__main__':
    main(sys.argv)
