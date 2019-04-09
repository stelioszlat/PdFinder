import org.apache.pdfbox.pdmodel.PDDocument;
import org.apache.pdfbox.pdmodel.PDDocumentInformation;
import org.apache.pdfbox.text.PDFTextStripper;

import java.io.File;
import java.io.IOException;

public class Main {

    public static void main(String[] args) throws IOException {

        File pdf = new File("demo.pdf");
        PDDocument document = PDDocument.load(pdf);
        PDDocumentInformation info = document.getDocumentInformation();
        PDFTextStripper stripper = new PDFTextStripper();
        String text = stripper.getText(document);

        System.out.println("Author: " + info.getAuthor());
        System.out.println("Title: " + info.getTitle());
        System.out.println("Creator: " + info.getCreator());
        System.out.println("Subject: " + info.getSubject());
        System.out.println("Creation Date: " + info.getCreationDate());
        System.out.println("Modification Date: " + info.getModificationDate());
        System.out.println("Keywords: " + info.getKeywords());

        System.out.println("Text: " + text);

        document.close();

    }
}
