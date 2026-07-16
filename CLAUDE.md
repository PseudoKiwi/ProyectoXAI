# Escritura de papers (paper/)

La carpeta `paper/` contiene el/los papers del proyecto en LaTeX (IEEEtran, formato
conference, dos columnas). Esta guía aplica a cualquier trabajo de escritura o edición de
`.tex` dentro de `paper/`.

## Plantilla de referencia

El template de escritura oficial es **`paper/IEEE/conference_template.tex`** (IEEE
conference template). Antes de escribir o editar contenido en `paper/*.tex`, consultar
ese archivo directamente (no solo las reglas resumidas abajo) para resolver cualquier duda
de formato, estructura de heads, o convenciones no cubiertas aquí — es la fuente de verdad,
este resumen es solo un extracto. Reglas clave extraídas de esa plantilla, a respetar
siempre:

- Clase `\documentclass[conference]{IEEEtran}`, dos columnas. No alterar márgenes, anchos
  de columna, ni fuentes — son parte de la clase, no se tocan a mano.
- Los headings numerados (Section, Subsection) los genera LaTeX solo; nunca numerar
  manualmente. Un subhead solo se introduce si hay al menos dos sub-temas.
- Ecuaciones: numeradas consecutivamente con `\begin{equation}`/`\label`, referenciadas con
  `\eqref{}` (nunca "Eq. (3)" ni el número pelado). No usar `{eqnarray}` — usar `{align}` o
  `{IEEEeqnarray}`. Cada símbolo se define antes o inmediatamente después de la ecuación en
  la que aparece. `\label` va después del elemento que actualiza el contador (nunca antes).
- Figuras y tablas: caption de figura debajo de la figura, título de tabla arriba de la
  tabla. Insertarlas después de ser citadas en el texto, preferentemente en top/bottom de
  columna. Citarlas como "Fig.~\ref{fig}" / "Table~\ref{tab}" (con `~` para el espacio no
  separable), incluso al inicio de una oración.
- Unidades SI como primarias; no mezclar SI y CGS en una misma ecuación. Cero antes del
  punto decimal (`0.25`, no `.25`).
- Abreviaturas/acrónimos se definen la primera vez que aparecen en el texto, aunque ya se
  hayan definido en el abstract (IEEE, SI, ac, dc, etc. no requieren definición).
- Errores comunes a evitar (de la sección "Some Common Mistakes" de la plantilla): "data" es
  plural; no usar "essentially" por "approximately"/"effectively"; no confundir
  imply/infer, affect/effect, principal/principle; "et al." sin punto después de "et";
  "i.e." = "that is", "e.g." = "for example".
- Bibliografía vía BibTeX (`references.bib`), estilo `unsrt` (`\bibliographystyle{unsrt}`),
  que numera las referencias en orden de aparición en el texto (no alfabético) — así lo pide
  la plantilla IEEE ("number citations consecutively... as in \cite{b3}"). No hardcodear
  números de cita a mano.

## Paquetes y convenciones ya establecidas en este proyecto

Además de la plantilla base, `main.tex` fija estas convenciones propias del proyecto — mantenerlas al editar o agregar contenido:

- `\usepackage[english]{babel}` — el paper se escribe en inglés académico formal, sin
  contracciones.
- Figuras: PNG para gráficos/capturas (`\includegraphics`, carpeta `paper/images/`), SVG
  para diagramas vectoriales vía `\usepackage{svg}` + `\includesvg` (se compilan a
  `svg-inkscape/`).
- Bloques de código/prompts con `\usepackage{listings}` y el `\lstset` ya definido al inicio
  del documento (fondo gris claro, monoespaciado, sin numeración especial). Reusar ese
  `\lstset`, no redefinir estilos de listing ad hoc.
- Métodos y librerías técnicas en `\textbf{}` la primera vez que se nombran en una sección
  (p. ej. `\textbf{LIME}`, `\textbf{SHAP}`, `\textbf{PyTorch}`).
- Nombres de datasets/splits (`\textbf{train}`, `\textbf{test}`) también en negrita.
- Asistencia de LLMs en la redacción se declara explícitamente con cita a las herramientas
  usadas (ver entradas `anthropic2025claude` / `openai_chatgpt` en `references.bib`); esa
  declaración va en Experimental Setup (o Acknowledgment), nunca omitirse ni ocultarse.
- Todas las citas bibliográficas nuevas van a `references.bib`; no crear archivos `.bib`
  adicionales ni bibliografías inline.

## Estructura macro del paper (convención de este proyecto)

A diferencia del IEEE template genérico (que es libre en su organización), los papers de
este proyecto siguen el esquema típico de venues de ML/CV (CVPR-style), sin límite de
páginas por ahora:

1. **Abstract**
2. **Introduction** — motivación, problema, contexto mínimo necesario, y una lista explícita
   de *contributions* (bullets) al final de la sección.
3. **Related Work** — revisión de literatura en prosa, organizada por bloques temáticos
   (p. ej. knowledge distillation; attention-as-explanation; post-hoc explainability
   methods), cada bloque cerrando con la conexión al gap que este trabajo cubre. **No**
   contiene definiciones formales/ecuaciones extensas de los métodos usados — eso va en
   Experiments. Evitar que se convierta en un tutorial de background.
4. **Experiments** — reemplaza a Methodology + Results + Discussion como secciones
   separadas. Subsecciones típicas:
   - *Experimental Setup*: herramientas, modelos, datos, procedimiento de entrenamiento/
     evaluación, hardware.
   - *Metrics* (si aplica): definiciones formales necesarias para leer las tablas de
     resultados (esto es lo único "tipo background" que sí vive en Experiments, no en
     Related Work).
   - Resultados agrupados por experimento/pregunta, con la discusión de cada resultado
     **inmediatamente después** de presentarlo (no un bloque de Discussion separado y
     lejano). Preferir subsecciones como "Evaluation on X", "Functional Comparison",
     "Representational Comparison", etc., cada una con su propio breve análisis.
   - *Limitations*: subsección final, concentrando en un solo lugar las limitaciones del
     estudio (no repetirlas dispersas en Setup/Results/Conclusions).
5. **Conclusions** — síntesis breve (1-2 párrafos) + trabajo futuro. No repetir números ya
   discutidos en Experiments; solo la interpretación de alto nivel.
6. **References**
7. **Appendix** — resultados/figuras secundarias, derivaciones extensas que no son
   necesarias para seguir el argumento principal en el cuerpo del paper.

Al escribir contenido nuevo o reorganizar contenido existente, preservar los números,
resultados empíricos y citas tal cual están — reestructurar es sobre organización y prosa,
no sobre regenerar resultados.

## Documentos del paper: `main.tex` vs `revised.tex`

Este proyecto mantiene **dos** archivos `.tex` con propósitos distintos, no intercambiables:

- **`main.tex`** — versión completa, sin límite de páginas. Es la versión de referencia:
  contiene todos los resultados, tablas completas (comparaciones layer-wise fila por fila),
  todas las figuras (LIME, SHAP, Integrated Gradients) y el Appendix. No se recorta para
  ganar espacio.
- **`revised.tex`** — versión condensada derivada de `main.tex`, con un **límite estricto de
  5 hojas incluyendo referencias** (formato IEEE conference, dos columnas). Para entrar en
  ese límite, prioriza mantener las afirmaciones y números centrales del paper mientras
  condensa agresivamente la prosa y reduce tablas/figuras a resúmenes representativos (p. ej.
  reportar solo capas representativas de una tabla layer-wise en vez de las 11 filas, fusionar
  tablas de métricas de un mismo modelo en una sola, combinar figuras relacionadas con
  `subcaption`/`figure*`, o resumir en prosa resultados que en `main.tex` tienen tabla propia).
  No se agrega un Appendix en `revised.tex` — si no entra en las 5 hojas, se resume en texto o
  se omite, señalando en una nota que la versión extendida (`main.tex`) tiene el detalle
  completo.

Reglas al tocar cualquiera de los dos:

- Nunca "portar" un recorte de `revised.tex` hacia `main.tex` ni viceversa sin que se pida
  explícitamente — son documentos con audiencias/propósitos distintos y pueden divergir en
  estructura y nivel de detalle.
- Si se corrige un dato, cifra o cita errónea, corregirla en **ambos** archivos (la
  corrección sí aplica a los dos; el recorte de contenido no).
- Antes de recortar contenido para `revised.tex`, no inventar ni recalcular números — los
  resúmenes/agregados que reemplazan una tabla completa deben derivarse de los valores ya
  presentes en `main.tex`.
- Verificar el límite de páginas compilando (`latexmk -pdf`) y contando las páginas del PDF
  resultante, no estimando a ojo.
