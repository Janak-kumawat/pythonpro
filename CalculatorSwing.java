import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class CalculatorSwing extends JFrame implements ActionListener {
    JTextField display;
    String operator = "";
    double firstNumber = 0;

    public CalculatorSwing() {
        setTitle("Calculator");
        setLayout(new BorderLayout());
        setSize(400, 500);
        setDefaultCloseOperation(EXIT_ON_CLOSE);

        display = new JTextField("0");
        display.setFont(new Font("Arial", Font.PLAIN, 20));
        add(display, BorderLayout.NORTH);

        JPanel panel = new JPanel(new GridLayout(4, 4));
        String[] buttons = {
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "0", ".", "=", "+"
        };

        for (String b : buttons) {
            JButton btn = new JButton(b);
            btn.addActionListener(this);
            panel.add(btn);
        }

        add(panel, BorderLayout.CENTER);
        setVisible(true);
    }

    public void actionPerformed(ActionEvent e) {
        String cmd = e.getActionCommand();

        if ("0123456789.".contains(cmd)) {
            if (display.getText().equals("0")) {
                display.setText(cmd);
            } else {
                display.setText(display.getText() + cmd);
            }
        } else if ("+-*/".contains(cmd)) {
            operator = cmd;
            firstNumber = Double.parseDouble(display.getText());
            display.setText("0");
        } else if (cmd.equals("=")) {
            double secondNumber = Double.parseDouble(display.getText());
            double result = 0;
            switch (operator) {
                case "+": result = firstNumber + secondNumber; break;
                case "-": result = firstNumber - secondNumber; break;
                case "*": result = firstNumber * secondNumber; break;
                case "/": result = firstNumber / secondNumber; break;
            }
            display.setText("" + result);
        }
    }

    public static void main(String[] args) {
        new CalculatorSwing();
    }
}
