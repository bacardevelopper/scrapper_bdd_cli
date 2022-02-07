from func_tools import exec_cmd

# --
def main():
    while True:
        commandes_recup = input('INSTRCUTIONS : ')
        exec_cmd.cli_interpreter(commandes_recup)
    
if __name__ == "__main__":
    main()