package fileIO;

import java.io.File;
import java.io.IOException;

public class CreateFile {

	public static void main(String[] args) {
		try {
			//uses only java.io.File
			File f = new File("test.txt");
			if(f.createNewFile()) {
				System.out.println("File Created");
			}
			else {
				System.out.println("File already exists");
			}
		}catch(IOException e) {
			e.printStackTrace();
		}
	}

}
