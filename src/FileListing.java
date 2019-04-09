import java.io.File;
import java.nio.file.Paths;
import java.util.ArrayList;

public class FileListing {

    private ArrayList<File> files = new ArrayList<>();

    public ArrayList<File> listDir(Paths path){
        return files;
    }

    private boolean identifyPdf(String file){
        return true;
    }

    public void listFound(){
        System.out.println(files);
    }

    public void listAllIn(Paths path){

    }

    public void listAll(){

    }

    public void find(String title){

    }

    public void findAllIn(Paths path){

    }

    public void findAll(){

    }

    public File getFile(String title){
        return files.get(0);
    }

}
