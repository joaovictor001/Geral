import javax.swing.plaf.synth.SynthRadioButtonMenuItemUI;

public class Produto {
    String nome;
    double preco;
    double desconto;
    public Produto(String nome ){
        this.nome = nome;

    }
    public Produto(String nome,double preco){
        this.nome =nome;
        this.preco = preco;
    }

    public String retornaResulmoDoProduto(){
       return String.format("o Produto %s esta com o preço de %.2f", nome,preco);
    }
    public double retornaPrecoComDesconto(){
        return preco - (preco * desconto);

    }

    public void  imprimirResulmoDoProduto(){
        System.out.println(String.format("o Produto %s esta com o preço de %.2f", nome,preco));
    }

}
