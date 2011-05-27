# copypasted from PHP implementation http://www.nitrxgen.net/source/?file=bubblebabble

def transcode(numbers):
    V = 'aeiouy'
    C = 'bcdfghklmnprstvzx'
    result = []
    for i in range(0, len(numbers), 5):
        a, b, c, d, e = numbers[i:i+5]
        result.append(C[a] + V[b] + C[c] + V[d] + C[e])
    return '-'.join(result)

def babble(numbers):
    result = [16]
    seed = 1
    i = 0
    while True:
        if i >= len(numbers):
            result.extend([ 
                seed % 6, 
                16, 
                seed // 6,
            ])
            break
        
        byte1 = numbers[i]
        result.extend([ 
            (((byte1 >> 6) & 3) + seed) % 6, 
            (byte1 >> 2) & 15, 
            ((byte1 & 3) + (seed // 6)) % 6,
        ])

        if i+1 >= len(numbers):
            break
        
        byte2 = numbers[i+1]
        result.extend([
            (byte2 >> 4) & 15,
            byte2 & 15
        ])
        
        seed = (seed * 5 + byte1 * 7 + byte2) % 36
        i += 2
    result.append(16)
    return transcode(result)
    
def babbleStr(s):
    return babble([ord(c) for c in s])
    
checks = {
    '' : 'xexax', 
    '1234567890' : 'xesef-disof-gytuf-katof-movif-baxux', 
    'Pineapple' : 'xigak-nyryk-humil-bosek-sonax', 
    'asdf' : 'ximel-finek-koxex', 
    'Testing a sentence.' : 'xihak-hysul-gapak-venyd-bumud-besek-heryl-gynek-vumuk-hyrox',
}
if __name__ == '__main__':
    for sin, sout in checks.items():
        bbl = babbleStr(sin)
        answer = {
            True:  'correct:     ', 
            False: 'NOT correct: ',
        }
        print('%s"%s" -> "%s" (sample is "%s")' % (answer[bbl == sout], sin, bbl, sout))
