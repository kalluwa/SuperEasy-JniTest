import java.io.FileWriter;
import java.io.IOException;

public class JniTest
{
    //load library
    static 
    {
        System.loadLibrary("HelloJni");
    }
    
    public native int add(int a,int b);
    public native byte[] modifybytes(byte[] data,int width,int height);

    public void printMat(byte[] raw,int width,int height)
    {
        System.out.println("\nmatrix data is");
        for(int i=0;i<height;i++)
        {
            for(int j=0;j<width;j++)
            {
                System.out.print(raw[i*width + j] & 0xFF);
                System.out.print('\t');

            }
            System.out.print('\n');
        }
    }
    public static void main(String[] args)
    {
        //System.out.println(new JniTest().add(3,4));

        var tobj = new JniTest();

        int width = 800;
        int height =600;
        
        byte[] raw = new byte[width*height*4];
        
        System.out.println(raw.length);
        //tobj.printMat(raw,2,2);
        byte[] screen_fb = tobj.modifybytes(raw,width,height);
        //tobj.printMat(bytes,2,2);

        System.out.println("write to file");
        System.out.println(screen_fb.length);
        try {
            FileWriter writer = new FileWriter("MyFile.ppm", true);

            writer.write(String.format("P3\n%d %d\n%d\n", width, height, 255));
            for (int i = 0; i<width*height; i++) 
            {
                //System.out.println(String.format("%d %d : %d",i/width,i%width,screen_fb[4*i+0]));
                writer.write(String.format("%d %d %d ", screen_fb[4*i+2]&0xff, screen_fb[4 * i + 1]&0xff, screen_fb[4 * i + 0]&0xff));
                writer.flush();
            }
            writer.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
        
        //System.out.println(String.format("%s %d","last red byte is ",screen_fb[256*255+0] & 0xff));
        System.out.println("---");
    }
}