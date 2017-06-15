input_prompt = ("Please enter an IP address. \n An IP address consists of 4 numbers, "
                "\n separated from each other with a full stop: ")
ipAddress = input(input_prompt)
if ipAddress[-1] != '.':
    ipAddress += '.'

segment = 1
segment_length = 0
# character = ""

for character in ipAddress:
    if character == '.':
        print("segment {} contains {} characters".format(segment, segment_length))
        segment += 1
        segment_length = 0
    else:
        segment_length += 1
#at this moment, the code reads the three most left handed segments. but it forgets to read and check the last segment.
#just becuz it has no dots in the end of it. to solving this freaky problem we have to use a sneaky trick!

# unless the final character in the string was a . then we haven't printed the last segment
if character != '.':
    print("segment {} contains {} characters".format(segment, segment_length))

