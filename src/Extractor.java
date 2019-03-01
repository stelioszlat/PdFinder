import org.apache.pdfbox.pdmodel.PDDocument;
import org.apache.pdfbox.text.PDFTextStripper;

import java.io.File;
import java.io.IOException;
import java.util.ArrayList;
import java.util.GregorianCalendar;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Extractor implements Runnable{

    private PDDocument doc;

    public void extract(PDDocument doc) {
        this.doc = doc;
        this.run();
    }

    private void findKeywords(String text, ArrayList<String> keywords){
        Pattern t = Pattern.compile(text);
        Matcher m;
    }

    @Override
    public void run(){
        try {
            PDFTextStripper strip = new PDFTextStripper();
            String text = strip.getText(this.doc);

        }
        catch(IOException e){
            e.printStackTrace();
        }
    }
}
