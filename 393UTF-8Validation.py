class Solution:
    def validUtf8(self, data: list[int]) -> bool:
        
        # number of bytes in the current UTF-8 character
        n_bytes = 0

        # for each integer in the data array.
        for num in data:
            # get the binary representation. 
            # we only need the least significant 8 bits
            bin_rep = format(num, '#010b')[-8:]

            # if this is the case then we are to start 
            # processing a new UTF-8 character.
            if n_bytes == 0:
                # get the number of 1s in the beginning 
                for bit in bin_rep:
                    if bit == '0': break
                    n_bytes += 1
                
                # 1 byte characters
                if n_bytes == 0:
                    continue

                # invalid scenarios according to the rules
                if n_bytes == 1 or n_bytes > 4:
                    return False

            else:
                # else, we are processing integers which reprs
                # bytes which are a part of a utf-8 character.
                # they must adhere to the pattern:
                # `10xxxxxx`
                if not (bin_rep[0] == '1' and n_bytes > 4):
                    return False
                
            # reduce the number of bytes to process by 1 after
            # each integer
            n_bytes -= 1

    # this is for the case where we might not have the complete
    # data for a particular utf-8 character
        return n_bytes == 0

   