class subnet_calculation():

    def verify_IP(start, end, hosts):
        print(hosts)
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
        for i in range(len(startIP)):
            count += 1
            if startIP[i] in validNum:
                isValid.append(startIP[i])
            elif startIP[i] == "." and count <= 4 and count > 1:
                isValid.append(startIP[i])
                count = 0
            elif count > 3 or startIP[i] not in validNum or count == 1:
                answer.append("not valid")
                break
            if i == (len(startIP) - 1):
                answer.append("valid")
        count = 0
        for i in range(len(endIP)):
            count += 1
            if endIP[i] in validNum:
                isValid.append(endIP[i])
            elif endIP[i] == "." and count <= 4 and count > 1:
                isValid.append(endIP[i])
                count = 0
            elif count > 3 or end[i] not in validNum or count == 1:
                answer.append("not valid")
                break
            if i == (len(endIP) - 1):
                answer.append("valid")
        print("instance check", isinstance(hosts, str))
        if isinstance(hosts, int) and hosts > 0 and hosts < 65536:
            answer.append("valid")
        else:
            answer.append("not valid")
        return answer
    def calculateMask(start, end, hosts):
        print("made it to calculateMask!")
print(subnet_calculation.verify_IP('192', '168', '123'))
