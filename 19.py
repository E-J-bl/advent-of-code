instructions = [la.strip("\n") for la in open('input.txt', "r").readlines()]
print(instructions)
ll = [x for x in open('input.txt').read().strip().split('\n\n')]
workflow, parts = ll
workflow = {l.split("{")[0]: l.split("{")[1][:-1] for l in workflow.split("\n")}
data = instructions[instructions.index("") + 1:]
'''part1 note that you need to add the functions A{} and R{} to the input to make it work. strange quirk but got me throught p1
print(data)
instructions = instructions[0:instructions.index("")]
inst = []
for la in instructions:
    la = la[0:-1]
    temp = la.split("{")
    temp[1] = temp[1].split(",")
    temp2 = []
    for con in temp[1]:
        temp2.append(con.split(":"))
    temp[1] = temp2
    inst.append(temp)
funcname = [na[0] for na in inst]

for ind, ob in enumerate(data):
    data[ind] = ob[1:-1].split(",")


def complexsetsort(sets, sorterValue=0):
    unsorted = True
    sortcheck = 0
    while unsorted:
        sortcount = 0
        for i in range(len(sets) - 1):
            if int(sets[i][sorterValue]) > int(sets[i + 1][sorterValue]):
                sets[i], sets[i + 1] = sets[i + 1], sets[i]
                sortcount += 1
        if sortcount == 0:
            sortcheck += 1
            if sortcheck == 3:
                unsorted = False
    return sets


def sumsa(point):
    sum = 0
    prop = {"x": int(point[0][point[0].index("=") + 1:]), "m": int(point[1][point[1].index("=") + 1:]),
            "a": int(point[2][point[2].index("=") + 1:]), "s": int(point[3][point[3].index("=") + 1:])}
    for val in prop.values():
        sum += val
    return sum


def mapchecker(ob):
    # P1
    total = 0
    acc_or_req = False
    prop = {"x": int(ob[0][ob[0].index("=") + 1:]), "m": int(ob[1][ob[1].index("=") + 1:]),
            "a": int(ob[2][ob[2].index("=") + 1:]), "s": int(ob[3][ob[3].index("=") + 1:])}
    # print(prop)
    curent_inst = funcname.index("in")
    while not acc_or_req:
        # print(f"current{curent_inst}")
        # print(f"fuction{inst[curent_inst]}")
        for check in inst[curent_inst][1]:
            # print(f"check{check}")
            if len(check) == 1:
                curent_inst = funcname.index(check[0])
                # print(f"reached end")
                break
            else:
                dep = prop[check[0][0]]
                if check[0][1] == ">":
                    if dep > int(check[0][check[0].index(">") + 1:]):
                        curent_inst = funcname.index(check[1])
                        break
                else:
                    if check[0][1] == "<":
                        if dep < int(check[0][check[0].index("<") + 1:]):
                            curent_inst = funcname.index(check[1])
                            break
        if curent_inst == funcname.index("A") or curent_inst == funcname.index("R"):
            acc_or_req = True

            if curent_inst == funcname.index("A"):
                total += sumsa(ob)
                # total+=1
    return total


def possiblesplit(inst):
    numbersinlist = []
    for function in inst:
        for command in function[1]:
            if len(command) == 1:
                continue
            else:
                numbersinlist.append([command[0][0], int(command[0][2:]), command[0][1]])
    return numbersinlist


to = 0
for ob in data:
    to += mapchecker(ob)
print(inst)
print(data)
print(to)'''


# completely rewrote this for part2 so i could work with functions instead of the mess that is above
# also the code above is created using wierd formatting that i could not understand 20 min after i worked on it 
# so i completely redid it. it was faster than understanding it
# the code below is not the original code. it is code i worked on to get it to actually run in time
# and then spend 2 hours working on it to make it readable


def maper(part, instruction):
    w = workflow[instruction]
    print(f"workflow: {w}")
    x, m, a, s = part
    for it in w.split(","):
        if it == "R":
            return False
        if it == "A":
            return True
        if ":" not in it:
            return maper(part, it)
        cond = it.split(":")[0]
        if eval(cond):
            if it.split(":")[1] == "R":
                return False
            if it.split(":")[1] == "A":
                return True
            return maper(part, it.split(":")[1])


def both(dot, greater, val, ranges):
    dot = 'xmas'.index(dot)
    ranges2 = []
    for r in ranges:
        r = list(r)
        lo, hi = r[dot]
        if greater:
            lo = max(lo, val + 1)
        else:
            hi = min(hi, val - 1)
        if lo > hi:
            continue
        r[dot] = (lo, hi)
        ranges2.append(list(r))
    return ranges2


def acceptance_ranges_outer(work):
    return acceptance_ranges_inner(workflow[work].split(","))


def acceptance_ranges_inner(w):
    it = w[0]
    if it == "R":
        return []
    if it == "A":
        return [((1, 4000), (1, 4000), (1, 4000), (1, 4000))]
    if ":" not in it:
        return acceptance_ranges_outer(it)
    cond = it.split(":")[0]
    greater = ">" in cond
    dot = cond[0]
    val = int(cond[2:])
    val_inverted = val + 1 if greater else val - 1
    if_cond_is_true = both(dot, greater, val, acceptance_ranges_inner([it.split(":")[1]]))
    if_cond_is_false = both(dot, not greater, val_inverted, acceptance_ranges_inner(w[1:]))
    return if_cond_is_true + if_cond_is_false


p2 = 0
for rng in acceptance_ranges_outer('in'):
    temp = 1
    for lo, hi in rng:
        temp *= hi - lo + 1
    p2 += temp
#miles be greatfull i decided to kill a night for this because otherwise your computer would melt like mine did

print(p2)
