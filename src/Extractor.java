import org.apache.pdfbox.pdmodel.PDDocument;
import org.apache.pdfbox.text.PDFTextStripper;

import java.io.File;
import java.io.IOException;
import java.util.GregorianCalendar;

public class Extractor{

    public String extract(PDDocument doc) throws IOException{

        PDFTextStripper strip = new PDFTextStripper();
        return strip.getText(doc);
    }

}
