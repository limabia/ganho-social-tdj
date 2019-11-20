
package gerador_testes;

import java.io.FileWriter;
import java.io.IOException;

public class GeradorDeTestes {
    
    // Deve possuir a barra no final do nome
    private final String localDeSalvamento;
    private final String[] opcoes = {"baixa", "media", "alta"};
    
    public GeradorDeTestes(String localDeSalvamento) {
        if(localDeSalvamento == null) {
            this.localDeSalvamento = "";
        } else {
            this.localDeSalvamento = localDeSalvamento;
        }
    }

    public void gerarTesteGeral(final int quantidadeDeCadaPerfil) {
        final String nomeDoArquivo = "01_" + quantidadeDeCadaPerfil + "_perfis_teste-geral.txt";
        final String CaminhoDoArquivo = this.localDeSalvamento + nomeDoArquivo;
      
        int contador = 1;
        
        try(FileWriter escritor = new FileWriter(CaminhoDoArquivo)) {
            for(String varConteudoInterassado : this.opcoes) {
                for(String varConteudoPublicado : this.opcoes) {
                    for(String qualidade : this.opcoes) {
                        for(String frequencia : this.opcoes) {
                            for(int i = 0; i < quantidadeDeCadaPerfil; i++) {
                                String nome = "perfil_" + contador;

                                String perfil = nome + ","
                                        + varConteudoInterassado + ","
                                        + varConteudoPublicado + ","
                                        + qualidade + ","
                                        + frequencia;
                                
                                escritor.write(perfil + "\n");
                                contador++;
                            }
                        }
                    }
                }
            }
            escritor.close();
        } catch(IOException ioe) {
            throw new RuntimeException("Nao eh possivel executar o teste geral (" + nomeDoArquivo + "):" + ioe.getMessage());
        }
    }
    
    public void gerarTesteDeExtremos(final int quantidadeDeCadaPerfil) {
        final String nomeDoArquivo = "02_" + quantidadeDeCadaPerfil + "_perfis_teste-extremo.txt";
        final String CaminhoDoArquivo = this.localDeSalvamento + nomeDoArquivo;

        int contador = 1;
        
        try(FileWriter escritor = new FileWriter(CaminhoDoArquivo)) {
            for(String opcao : opcoes) {
                String varConteudoInterassado = opcao;
                String varConteudoPublicado = opcao;
                String qualidade = opcao;
                String frequencia = opcao;
            
                for(int i = 0; i < quantidadeDeCadaPerfil; i++) {
                    String nome = "perfil_" + contador;

                    String perfil = nome + ","
                            + varConteudoInterassado + ","
                            + varConteudoPublicado + ","
                            + qualidade + ","
                            + frequencia;

                    escritor.write(perfil + "\n");
                    contador++;
                }
            }
            escritor.close();
        } catch(IOException ioe) {
            throw new RuntimeException("Nao eh possivel executar os testess extremos (" + nomeDoArquivo + "):" + ioe.getMessage());
        }
    }
    
    
    public void gerarTodosOsTestes() {
    
        int[] quantidadesTesteGeral = {10, 100, 500, 1000};
        for(int quantidade : quantidadesTesteGeral) {
            this.gerarTesteGeral(quantidade);
        }
        
        int[] quantidadesTesteExtremo = {10, 50, 100, 500};
        for(int quantidade : quantidadesTesteExtremo) {
            this.gerarTesteDeExtremos(quantidade);
        }
    }
    
    public static void main(String[] args) {
        String localDeSalvamento = "";
        if(args.length > 0) {
            localDeSalvamento = args[0];
        } else {
            localDeSalvamento = "src/testes/";
        }
        
        GeradorDeTestes geradorDeTestes = new GeradorDeTestes(localDeSalvamento);
        geradorDeTestes.gerarTodosOsTestes();
    }
}
