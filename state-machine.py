from libdw import sm
#
# class CM(sm.SM):
#     start_state = 0
#     def get_next_values(self,state, inp):
#         print("state:", state)
#         if state == 0 and inp == 50:
#             return (1, (50, '--',0))
#         if state == 1 and inp == 50:
#             return (0, (0, 'coke',0))
#         if state == 1 and inp == 100:
#             return (0, (0,'coke',50))
#         if state == 0 and inp == 100:
#             return (0, (0,'coke',0))
#         else:
#             return (state, (0,'--',inp))
#
# #
# c = CM()
# c.start()
# print(c.step(50))
# print(c.state)
# print(c.step(10))
# print(c.state)

#
# class SimpleAccount(sm.SM):
#     def __init__(self, start_deposit):
#         self.start_state = start_deposit
#
#     def get_next_values(self, state, inp):
#
#         if state < 100 and inp < 0:
#             state = state + inp - 5
#             return state, state
#         else:
#             state = state + inp
#             return state, state
#
# acct = SimpleAccount(110)
#
# acct.start()
#
# print(acct.step(10))

# Not comment
class CommentsSM(sm.SM):
    start_state = 0
    def get_next_values(self, state, inp):
        if state == 0 and inp != '#':
         return (0, None)
        if state == 0 and inp == '#':
         return (1, inp)
        if state == 1 and inp !='\n':
         return (1, inp)
        if state == 1 and inp == '\n':
         return (0, None)

str = "def f(x): #comment\n return 1"

m = CommentsSM()

print(m.transduce(str, verbose=True))


from libdw import sm
# State 0 default, first word
# State 1 reading first word
# State 2 finsh reading first word
class FirstWordSM(sm.SM):
    start_state = 0
    def get_next_values(self, state, inp):
        if state == 0 and inp in [' ','\n']:
         return (0, None)
        if state == 0 and inp not in [' ','\n']:
         return (1, inp)
        if state == 1 and inp == ' ':
         return (2, None)
        if state == 1 and inp != ' ':
         return (1, inp)
        if state == 2 and inp !='\n':
         return (2, None)
        if state == 2 and inp == '\n':
         return (0, None)

class Turnstile(sm.SM):
  start_state = 'locked'
  def get_next_values(self, state, inp):
    if state == 'locked':
      if inp == 'coin':
        return ('unlocked', 'enter')
      else:
        return ('locked', 'pay')
    else:
      if inp == 'turn':
        return ('locked', 'pay')
      else:
        return ('unlocked', 'enter')