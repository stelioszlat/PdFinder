import java.util.ArrayList;
import java.util.Date;

// used only when extracting scientific papers
public class PdfFile {
    private String title;
    private ArrayList<String> authors;
    private String abstr; // abstract;
    private ArrayList<Keyword> keywords;
    private Date pubDate; // published date
    private double weight;

    public double getWeight() {
        return weight;
    }

    public void setWeight(double weight) {
        if(weight > 0 && weight < 1) {     // weight is a percentage, can't be 100% nor 0%
            this.weight = weight;
        }
    }


}
