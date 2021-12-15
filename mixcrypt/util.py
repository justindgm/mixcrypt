def float_to_binary(array):
    sign_array = cp.signbit(array)
    array = cp.abs(array).view(cp.uint32)
    exponent_array = (((array & 0b01111111100000000000000000000000) >> 23) - 127).astype(cp.uint8) # TODO: interpret as uint or int?
    mantissa_array = (array & 0b00000000011111111111111111111111) | 0b00000000100000000000000000000000 # OR for implicit bit
    return sign_array, exponent_array, mantissa_array
