class Request:
    MOVE_L = 'm_l'
    MOVE_R = 'm_r'
    MOVE_U = 'm_u'
    MOVE_D = 'm_d'
    MOVE_UL = 'm_ul'
    MOVE_UR = 'm_ur'
    MOVE_DL = 'm_dl'
    MOVE_DR = 'm_dr'
    MOVE_US = 'm_us'
    MOVE_DS = 'm_ds'
    HELP = 'help'
    READ = 'read'
    LOOK = 'look'
    EXAMINE = 'exam'
    USE = 'use'
    WIELD = 'wield'
    UNWIELD = 'unwield'
    WEAR = 'wear'
    UNWEAR = 'unwear'
    CONSUME = 'consume'
    ATTACK = 'atk'
    DEFEND = 'def'
    SPELL = 'spell'
    THROW = 'throw'
    FLEE = 'flee'
    BUY = 'buy'
    SELL = 'sell'

    def __init__(self, type, params = None):
        self.type = type
        self.params = params



