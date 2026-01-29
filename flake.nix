{
  description = "Humanitarian Reporting Tool Environment";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
  };

  outputs = { self, nixpkgs }:
    let
      system = "x86_64-linux";
      pkgs = nixpkgs.legacyPackages.${system};
    in
    {
      devShells.${system}.default = pkgs.mkShell {
        buildInputs = with pkgs; [
          (python3.withPackages (ps: with ps; [
            pandas
            numpy
            fpdf
            openpyxl
          ]))
        ];

        shellHook = ''
          echo "🚀 Ambiente Python (NixOS) carregado com sucesso!"
          echo "As bibliotecas Pandas, FPDF e OpenPyXL já estão prontas."
        '';
      };
    };
}
