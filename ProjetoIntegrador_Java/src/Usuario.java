import java.util.Calendar;
import java.util.Date;
import java.util.Random;

public class Usuario {
    private String id = "";
    private String nomeproduto = "";
    private String valor = "";
    private String categoria = "";
    private Date dataCadastro;

    public Usuario(String nomeproduto, String valor, String categoria){

        //#

        this.id = ""+gerarId();
        this.nomeproduto = nomeproduto;
        this.valor = valor;
        this.categoria = categoria;
        this.dataCadastro = Calendar.getInstance().getTime();
    }

    public String getId() {
        return this.id;
    }

    public String getNomeproduto() {
        return this.nomeproduto;
    }

    public void setNomeproduto(String nomeproduto) {
        this.nomeproduto = nomeproduto;
    }

    public String getValor() {
        return this.valor;
    }

    public void setValor(String valor) {
        this.valor = valor;
    }

    public String getCategoria() {
        return this.categoria;
    }

    public void setCategoria(String categoria) {
        this.categoria = categoria;
    }

    public Date getDataCadastro() {
        return this.dataCadastro;
    }

    public void setDataCadastro(Date dataCadastro) {
        this.dataCadastro = dataCadastro;
    }

    private int gerarId(){
        Random numeroAleatorio = new Random();
        return numeroAleatorio.nextInt(2000);
    }

}
