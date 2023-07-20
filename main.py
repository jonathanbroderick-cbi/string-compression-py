# Rules
#  1. This is open book - feel free to search the web or consult documentation as necessary
#  2. Think out loud - a big part of this is getting a feel for your thought process
#  3. Run the code as often as you'd like - failing is fine
#  4. You can add more test cases if needed


# This function should compress a string like so:
#   compress("aaaabbCdddaaaaa") == "a4bbCd3a5"
#
def compress(inputStr = ""):
    return


#############
#           #
#   Tests   #
#           #
#############
def test(inputStr, expected):
    print("[test] " + inputStr + " => " + expected)

    result = compress(inputStr)

    if result == expected:
        print("  ✅  passed")
    else:
        print("  ❌  failed")
        print("  Result:   " + result)
        print("  Expected: " + expected)

    print()

test("aaaabbCdddaaaaa", "a4bbCd3a5")
