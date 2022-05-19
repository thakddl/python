package application;
   
import javafx.application.Application;
import javafx.stage.Stage;
import javafx.scene.Scene;
import javafx.scene.layout.BorderPane;
import javafx.event.Event;
import javafx.event.EventHandler;
import javafx.fxml.FXMLLoader;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.TextField;
import javafx.scene.layout.AnchorPane;


public class Main3 extends Application {
   @Override
   public void start(Stage primaryStage) {
      try {
         AnchorPane root = (AnchorPane)FXMLLoader.load(getClass().getResource("Main3.fxml"));
         Scene scene = new Scene(root,400,400);
         scene.getStylesheets().add(getClass().getResource("application.css").toExternalForm());
         primaryStage.setScene(scene);
         primaryStage.show();
         
         Button btn = (Button) scene.lookup("#btn");
         TextField tf01 = (TextField) scene.lookup("#tf01");
         TextField tf02 = (TextField) scene.lookup("#tf02");
         TextField tf03 = (TextField) scene.lookup("#tf03");
         btn.setOnMouseClicked(new EventHandler<Event>() {
            @Override
            public void handle(Event event) {
               
               int i =  Integer.parseInt(tf01.getText())
            		   +Integer.parseInt(tf02.getText());
               
               tf03.setText(String.valueOf(i));
            	
            }
         });
         
                
      } catch(Exception e) {
         e.printStackTrace();
      }
   }
   
   public static void main(String[] args) {
      launch(args);
   }
}