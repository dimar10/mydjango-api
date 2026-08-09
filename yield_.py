def read(filepath):
    with open(filepath,'r',encoding='utf-8',errors='replace') as f:
        for line in f:
            yield line.rstrip('\n')

def filter_errors(lines):
    for line in lines:
        if 'ERROR' in line:
            yield line

def writeline(lines,out_path):
    with open(out_path,'w',encoding='utf-8') as f:
        for line in lines:
            f.write(line + '\n')

pipe = filter_errors(read('app.log'))
writeline(pipe,'errors_only.log')