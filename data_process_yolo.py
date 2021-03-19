import re
import os
import argparse

def data_process(args):
  f=os.popen("cat "+args).read()
  raw_f=f.split("\n")
  FPS = []
  count = 0
  for line in raw_f:
    pattern=re.compile(r'FPS:\d+.\d')
    set=pattern.findall(line)
    if len(set) > 0:
        fps = set[0]
        pattern = re.compile(r'\d+.\d+')
        value_raw = float(pattern.findall(fps)[0])
        FPS.append(value_raw)
        if value_raw < 20.0:
            count += 1 # miss
  # print(FPS)
#   print("Average FPS: {}".format(sum(FPS)/len(FPS)))
#   print("Min/Max FPS: {}, {}".format(min(FPS), max(FPS)))
  
  return sum(FPS)/len(FPS), min(FPS), max(FPS), count / len(FPS)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('name', help='file name', default='')

    args = parser.parse_args()
    
    print("avg min max")
    # 1 inst
    avg1, minv1, maxv1, pmiss1 = data_process("test-1.txt")
    print("1 inst: {}, {}, {}, {}".format(avg1, minv1, maxv1, pmiss1))
    
    # 2 inst
    avg1, minv1, maxv1, pmiss1 = data_process("test-2.1.txt")
    avg2, minv2, maxv2, pmiss2 = data_process("test-2.2.txt")
    print("2 inst: {}, {}, {}, {}".format((avg1+avg2)/2, min(minv1,minv2), max(maxv1,maxv2), (pmiss1+pmiss2)/2))

    # 3 inst
    avg1, minv1, maxv1, pmiss1 = data_process("test-3.1.txt")
    avg2, minv2, maxv2, pmiss2 = data_process("test-3.2.txt")
    avg3, minv3, maxv3, pmiss3 = data_process("test-3.3.txt")
    print("3 inst: {}, {}, {}, {}".format((avg1+avg2+avg3)/3, min(minv1,minv2,minv3), max(maxv1,maxv2,maxv3), (pmiss1+pmiss2+pmiss3)/3))
    
    # 4 inst
    avg1, minv1, maxv1, pmiss1 = data_process("test-4.1.txt")
    avg2, minv2, maxv2, pmiss2 = data_process("test-4.2.txt")
    avg3, minv3, maxv3, pmiss3 = data_process("test-4.3.txt")
    avg4, minv4, maxv4, pmiss4 = data_process("test-4.4.txt")
    print("4 inst: {}, {}, {}, {}".format((avg1+avg2+avg3+avg4)/4, min(minv1,minv2,minv3,minv4), max(maxv1,maxv2,maxv3,maxv4), (pmiss1+pmiss2+pmiss3+pmiss4)/4))
