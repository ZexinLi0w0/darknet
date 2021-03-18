import re
import os
import argparse

def data_process(args):
    f=os.popen("cat "+args).read()
    raw_f=f.split("\n")
    cpu = []
    gpu = []
    for line in raw_f:
        cpu_value=0
        gpu_value=0
        cpu_pattern=re.compile(r'\[([^\[\]]*)\]')
        cpu_set=cpu_pattern.findall(line)
        if len(cpu_set) > 0:
            cpu_set=cpu_set[0]
            pattern=re.compile(r'\d+%@')
            cpu_value_raw=pattern.findall(cpu_set)
            for value in cpu_value_raw:
                cpu_value += float(re.compile(r'\d+').findall(value)[0])
        else:
            break

        gpu_pattern=re.compile(r'GR3D_FREQ \d+%@')
        gpu_set=gpu_pattern.findall(line)
        if len(gpu_set) > 0:
            gpu_set=gpu_set[0]
            pattern=re.compile(r'\d+%@')
            gpu_value_raw=pattern.findall(gpu_set)[0]
            gpu_value += float(re.compile(r'\d+').findall(gpu_value_raw)[0])

        if cpu_value > 100:
            cpu.append(cpu_value)
            gpu.append(gpu_value)
    
    #print("average/max CPU: {}, {}".format(sum(cpu)/len(cpu),max(cpu)))
    #print("average/max GPU: {}, {}".format(sum(gpu)/len(gpu),max(gpu)))

    return sum(cpu)/len(cpu), max(cpu), sum(gpu)/len(gpu), max(gpu)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('name', help='file name')

    args = parser.parse_args()

    print("cpu_avg, cpu_max, gpu_avg, gpu_max")
    
    # 1 inst
    cpu_avg, cpu_max, gpu_avg, gpu_max = data_process("yolov3-tiny-1inst.txt")
    print("1 inst: {}, {}, {}, {}".format(cpu_avg, cpu_max, gpu_avg, gpu_max))
    
    # 2 inst
    cpu_avg, cpu_max, gpu_avg, gpu_max = data_process("yolov3-tiny-2inst.txt")
    print("2 inst: {}, {}, {}, {}".format(cpu_avg, cpu_max, gpu_avg, gpu_max))

    # 3 inst
    cpu_avg, cpu_max, gpu_avg, gpu_max = data_process("yolov3-tiny-3inst.txt")
    print("3 inst: {}, {}, {}, {}".format(cpu_avg, cpu_max, gpu_avg, gpu_max))
    
    # 4 inst
    cpu_avg, cpu_max, gpu_avg, gpu_max = data_process("yolov3-tiny-4inst.txt")
    print("4 inst: {}, {}, {}, {}".format(cpu_avg, cpu_max, gpu_avg, gpu_max))

