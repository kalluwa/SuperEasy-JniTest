import os,sys
import shutil
import glob

def buildjavafile(javafile):
    if not javafile.endswith('.java'):
        return
            
    #测试代码文件
    javafilename = javafile
    #java bin目录
    javabindir = '\"C:/Program Files/Java/jdk-10.0.1/bin' 
    #vs2015 msbuild路径
    msbuildexe = '\"C:/Program Files (x86)/MSBuild/14.0/Bin/amd64/MSBuild.exe\"'

    #prapare
    projname = javafilename[:javafilename.rfind('.')]

    #1 java 2 class
    cmd = '%s -h c %s'%(javabindir+'/javac.exe\"',javafilename)
    #jdk 8
    #cmd = '%s %s'%(javabindir+'/javac.exe\"',javafilename)
    print(cmd)
    os.system(cmd)
    print("done!\n")

    #2 create header file [jdk 8]
    # cmd = ('%s %s'%(javabindir+'/javac.exe\" -h ',projname))
    # print(cmd)
    # os.system(cmd)
    # print("done!\n")

    #jdk 10
    c_headers = glob.glob("./c/*.h")
    for header in c_headers:
        if os.path.exists('./'+os.path.basename(header)):
            os.remove('./'+os.path.basename(header))
            
        shutil.move(header,'./')
    shutil.rmtree('./c')

    #before3 
    print('have you implement cpp file?')
    os.system('pause')
    #3 use msvc2015 to build dll
    #like
    # "C:\Program Files (x86)\MSBuild\14.0\Bin\amd64\MSBuild.exe" /p:Configuration=Release /p:Platform=x64
    cmd = ('%s /p:Configuration=Release /p:Platform=x64'%(msbuildexe))
    print(cmd)
    os.system(cmd)
    #3.5 copy dll to this folder
    dlls = glob.glob('./x64/Release/*.dll')
    for file in dlls:
        shutil.copy(file,'./')

    #4 build java and run
    #remove MyFile.ppm
    if os.path.exists('MyFile.ppm'):
        os.remove('MyFile.ppm')
        
    os.system('%s %s'%(javabindir+'/java.exe\"',projname))

    #5 remove 
    shutil.rmtree('./x64')

if __name__ == '__main__':
    if len(sys.argv) >1:
        buildjavafile(sys.argv[1])