# # should return True
# same_structure_as([ 1, 1, 1 ], [ 2, 2, 2 ] )
# same_structure_as([ 1, [ 1, 1 ] ], [ 2, [ 2, 2 ] ] )
#
# # should return False
# same_structure_as([ 1, [ 1, 1 ] ], [ [ 2, 2 ], 2 ] )
# same_structure_as([ 1, [ 1, 1 ] ], [ [ 2 ], 2 ] )
#
# # should return True
# same_structure_as([ [ [ ], [ ] ] ], [ [ [ ], [ ] ] ] )
#
# # should return False
# same_structure_as([ [ [ ], [ ] ] ], [ [ 1, 1 ] ] )


def same_structure_as(original, other):
    count_orig = len(original)
    count_other = len(other)
    if count_orig != count_other:
        return False

    for i in range(count_orig):
        orig_inst = isinstance(original[i], list)
        other_inst = isinstance(other[i], list)
        if orig_inst and other_inst:
            return same_structure_as(original[i], other[i])
        elif (orig_inst and not other_inst) or (not orig_inst and other_inst):
            return False

    return True


print(same_structure_as([1,5, 3, [1,1]],[2,2,2,[2, 2, []]]))
print(same_structure_as([ [ [ ], [ ] ] ], [ [ [ ], [ ] ] ] ))




