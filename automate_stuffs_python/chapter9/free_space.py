import os, getopt



def get_option_value(options, options_name, only_verify_names=False):

    for option in options:

        if option[0] in options_name:
            return True if only_verify_names else option[1]

    return False


if __name__ == "__main__":

    options,args = getopt.getopt("b:e:u:dyr",["between","unit=",""])

