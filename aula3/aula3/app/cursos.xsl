<?xml version="1.0" encoding="UTF-8"?>

<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:template match="curso">
            <h2><xsl:value-of select="nome"/></h2>
            <img>
                <xsl:attribute name="src">
                    <xsl:value-of select="imagem"/>
                </xsl:attribute>
            </img>
           <ul>
               <li><b>Guid: </b><xsl:value-of select="guid"/></li>
               <li><b> Codigo: </b><xsl:value-of select="codigo"/></li>
               <li><b>Director: </b></li>
                    <ul>
                        <xsl:for-each select="director">
                            <li>Nome: <xsl:value-of select="nome"/></li>
                            <li>Email: <xsl:value-of select="email"/></li>
                        </xsl:for-each>
                    </ul>
               
               <li><b> Grau: </b><xsl:value-of select="grau"/></li>
               <li><b> Duraçao: </b><xsl:value-of select="duracao"/></li>
               <li><b> Ano de inicio: </b><xsl:value-of select="ano_inicio"/></li>
               <li><b> Propinas: </b><xsl:value-of select="propinas"/></li>
               <li><b> Areas Cientificas:</b></li>
                    <ol>
                        <xsl:for-each select="areas">
                            <xsl:for-each select="area">
                                <li><xsl:value-of select="."/></li>
                            </xsl:for-each>
                        </xsl:for-each>
                    </ol>
               <li><b> Departamentos:</b></li>
                    <ol>
                        <xsl:for-each select="departamentos">
                            <xsl:for-each select="departamento">
                                <li>
                                    <a target="_blank">
                                        <xsl:attribute name="href">
                                            <xsl:value-of select="url"/>
                                        </xsl:attribute>
                                        <xsl:value-of select="nome"/>
                                    </a>
                                </li>
                            </xsl:for-each>
                        </xsl:for-each>
                    </ol>
               <li><b>Local: </b> <xsl:value-of select="local"/></li>
               <li><b>Acreditações: </b></li>
                    <ol>
                        <xsl:for-each select="acreditacoes">
                            <xsl:for-each select="acreditacao">
                                <li>
                                    <a target="_blank">
                                        <xsl:attribute name="href">
                                            <xsl:value-of select="url"/>
                                        </xsl:attribute>
                                        <xsl:value-of select="nome"/>
                                    </a>
                                </li>
                            </xsl:for-each>
                        </xsl:for-each>
                    </ol>
            </ul>
    </xsl:template>

</xsl:stylesheet>