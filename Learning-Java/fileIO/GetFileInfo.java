package fileIO;

import java.io.File;

public class GetFileInfo {

	public static void main(String[] args) {
		File f = new File("test.txt");
		if(f.exists()) {
			System.out.println("File name: " + f.getName());
			System.out.println("Absolute Path: " + f.getAbsolutePath());
			System.out.println("Writable: " + f.canWrite());
			System.out.println("Readable: " + f.canRead());
			System.out.println("File size in bytes: " + f.length());
		}
		else {
			System.out.println("File does not exists");
		}
	}

}
