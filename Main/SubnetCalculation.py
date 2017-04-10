class subnet_calculation():

    def verify_IP(start, end, hosts):
        container = [start, end]
        startIP = start
        endIP = end
        try:
            hosts = int(hosts)
        except (TypeError, ValueError) as e:
            print("cant convert", e)
        count = 0
        validNum = ["0","1","2","3","4","5","6","7","8","9"]
        isValid = [] # order stored [startIP, endIP, hosts] as either 'valid' or 'not valid'
        answer = []

        for IP in container:
            count = 0
            numCount = 0
            dotCount = 0
            IP_min = 7
            IP_max = 15
            validNum = ["0","1","2","3","4","5","6","7","8","9"]
            IPlist = []
            # following block splits IP at the dots and verifys that no octet is greater than 255
            # then counts the number of dots.
            newIP = IP.split(".")
            for i in newIP:
                if i == "":
                    answer.append("not valid")
                    break
                if int(i) > 255:
                    answer.append("not valid")
                    break
            for i in IP:
                if i == ".":
                    dotCount += 1
            if dotCount != 3:
                answer.append("not valid")
                break
            for i in IP:
                IPlist.append(str(i))

            # reset the counters to 0
            count = 0
            numCount = 0
            dotCount = 0

            #this block
            for i in range(len(IP)):
                if (count == 0 and IPlist[i] not in validNum):
                    answer.append("not valid")
                    break
                if (IPlist[i] in validNum and count >= 0):
                    if numCount > 4 and dotCount == 0:
                        print(numCount,IPlist[i],dotCount)
                        answer.append("not valid")
                        break
                    numCount += 1
                    count += 1
                if (IPlist[i] != "."):
                    numCount += 1
                elif (IPlist[i] == "." and count > 0):
                    try:
                        if IPlist[i + 1] == ".":
                            answer.append("not valid")
                            break
                    except:
                        pass
                    dotCount += 1
                    count +=1
                if (IPlist[i] not in validNum and IPlist[i] != "."):
                    answer.append("not valid")
                    break
            if dotCount > 3:
                answer.append("not valid")
                break
            if numCount < 4:
                answer.append("not valid")
                break
            if (len(IPlist) < IP_min or len(IPlist) > IP_max):
                answer.append("not valid")
                break
            answer.append("valid")

        if isinstance(hosts, int) and hosts > 0 and hosts < 65536:
            answer.append("valid")
        else:
            answer.append("not valid")
        return answer # needs to pass to Verify_Range if passing all previous tests (ex. 127.0.0.1 is not comparable against 192.168.0.1)
    def Verify_Range(start, end):

    def calculateMask(start, end, hosts):
