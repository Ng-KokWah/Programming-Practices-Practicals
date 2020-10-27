package fileIO;

import java.io.File;

public class DeleteFile {

	public static void main(String[] args) {
		File f = new File("test.txt");
		if(f.delete()) {
			System.out.println("File deleted!");
		}
		else {
			System.out.println("Failed to delete file!");
		}
	}

}
