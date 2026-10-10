type Pea = tuple[Pea] | None

def peano_to_int(p : Pea) -> int:
    match p:
        case None:
            return 0
        case (x,):
            return 1 + peano_to_int(x)

def peano_add(p1 : Pea, p2 : Pea) -> Pea:
    match p1:
        case None:
            return p2
        case (x,):
            return (peano_add(x, p2),)

p1 : Pea = (((None,),),) # 3
p2 : Pea = ((None,),) # 2
print(peano_to_int(peano_add(p1,p2)))
