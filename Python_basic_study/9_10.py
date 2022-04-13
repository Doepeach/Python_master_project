#일반 유닛
class Unit:
    def __init__(self,name,hp,speed):
        self.name=name
        self.hp=hp
        self.speed=speed
        print("{0} 유닛이 생성되었습니다".format(self.name))
    
    def move(self,location):
        print("{0}: {1} 방향으로 이동합니다. [속도 {2}]"\
            .format(self.name,location,self.speed))

    def damaged(self,damage):
        print("{0} : {1} 데미지를 입었습니다".format(self.name,damage))
        self.hp-=damage
        print("{0}: 현재 체력은 {1} 입니다.".format(self.name,self.hp))
        if self.hp<=0:
            print("{0}: 파괴되었습니다".format(self.name))

#공격 유닛
class AttackUnit(Unit):
    def __init__(self, name, hp, speed,damage):
        Unit.__init__(name, hp, speed)
        self.damage=damage
    
    def attack(self,location):
        print("{0}: {1} 방향으로 적군을 공격합니다. [공격력:{2}]"\
            .format(self.name,location,self.damage))

#마린
class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self,"마린",40,1,5)
    
    def stimpack(self):
        if self.hp>10:
            self.hp-=10
            print("{0}: 스팀팩을 사용합니다.(HP 10 감소)".format(self.name))
        else:
            print("{0}: 체력이 부족하여 스팀팩을 사용하지 않습니다".format(self.name))


    