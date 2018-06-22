#include "JniTest.h"
//https://blog.csdn.net/cmm0401/article/details/54599083
#include<stdlib.h>
#include "mini3d.h"

JNIEXPORT jint JNICALL Java_JniTest_add(JNIEnv *env, jobject obj, jint a, jint b)
{
	jint c = a + b;
	return c;
	printf("Hello Native World!\n");
}

JNIEXPORT jbyteArray JNICALL Java_JniTest_modifybytes
  (JNIEnv *env, jobject obj, jbyteArray data, jint width, jint height)
{
	//look here
	//https://docs.oracle.com/javase/7/docs/technotes/guides/jni/spec/functions.html

	int len = env->GetArrayLength(data);
	jbyte* bytesptr = env->GetByteArrayElements(data,0);

	// for(int i=0;i<height;i++)
	// {
	// 	for(int j=0;j<width;j++)
	// 	{
	// 		*(bytesptr+ i*width + j) = rand()%255;
	// 	}
	// }

	drawimage((unsigned char*)bytesptr,width,height);
	https://stackoverflow.com/questions/26603285/return-byte-array-in-jni-android
	env->SetByteArrayRegion(data,0,width*height*4,bytesptr);

	return data;
};