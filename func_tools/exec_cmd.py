from func_tools.class_tools import Tools
# ---------
cls_tools = Tools()

# fonctions
def les_commandes(cmd,options):
    if cmd == 'sub-push' and options !='':
        cls_tools.ajouter(options)
    elif cmd == 'sub-all':
        cls_tools.voir_tout()
        
def cli_interpreter(commands):
    commands_cli = commands.split(' ')
    liste_cmd = []
    for cmd in commands_cli:
        liste_cmd.append(cmd)
    
    if len(liste_cmd) == 2:
        les_commandes(liste_cmd[0],liste_cmd[1])
    elif len(liste_cmd) == 1:
        les_commandes(liste_cmd,'')
