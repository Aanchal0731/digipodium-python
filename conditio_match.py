message = input('Enter msg')

match msg:
    case "hlw":
        print('hy')
    case 'bye':
        print('gn')
    case 'ok':
        print('cool')
    case other:
        print('nothing to say about')