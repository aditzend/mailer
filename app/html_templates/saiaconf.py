from string import Template


template_saiaconf_1 = Template(
    """
<!DOCTYPE html>
<html
  xmlns:v="urn:schemas-microsoft-com:vml"
  xmlns:o="urn:schemas-microsoft-com:office:office"
  lang="en"
>
  <head>
    <title></title>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <!--[if mso
      ]><xml
        ><o:OfficeDocumentSettings
          ><o:PixelsPerInch>96</o:PixelsPerInch
          ><o:AllowPNG /></o:OfficeDocumentSettings></xml
    ><![endif]-->
    <style>
      @font-face {
        font-family: "Manrope";
        font-style: normal;
        font-weight: 500;
        font-display: swap;
        src: url(https://fonts.gstatic.com/s/manrope/v14/xn7gYHE41ni1AdIRggexSvfedN4.woff2)
          format("woff2");
        unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6,
          U+02DA, U+02DC, U+0304, U+0308, U+0329, U+2000-206F, U+2074, U+20AC,
          U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD;
      }

      @font-face {
        font-family: "Manrope";
        font-style: normal;
        font-weight: 200;
        font-display: swap;
        src: url(https://fonts.gstatic.com/s/manrope/v14/xn7gYHE41ni1AdIRggexSvfedN4.woff2)
          format("woff2");
        unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6,
          U+02DA, U+02DC, U+0304, U+0308, U+0329, U+2000-206F, U+2074, U+20AC,
          U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD;
      }
      * {
        box-sizing: border-box;
      }

      body {
        margin: 0;
        padding: 0;
      }

      a[x-apple-data-detectors] {
        color: inherit !important;
        text-decoration: inherit !important;
      }

      #MessageViewBody a {
        color: inherit;
        text-decoration: none;
      }

      p {
        line-height: inherit;
      }

      .desktop_hide,
      .desktop_hide table {
        mso-hide: all;
        display: none;
        max-height: 0px;
        overflow: hidden;
      }

      .image_block img + div {
        display: none;
      }

      @media (max-width: 670px) {
        .desktop_hide table.icons-inner,
        .social_block.desktop_hide .social-table {
          display: inline-block !important;
        }

        .icons-inner {
          text-align: center;
        }

        .icons-inner td {
          margin: 0 auto;
        }

        .image_block img.fullWidth {
          max-width: 100% !important;
        }

        .mobile_hide {
          display: none;
        }

        .row-content {
          width: 100% !important;
        }

        .stack .column {
          width: 100%;
          display: block;
        }

        .mobile_hide {
          min-height: 0;
          max-height: 0;
          max-width: 0;
          overflow: hidden;
          font-size: 0px;
        }

        .desktop_hide,
        .desktop_hide table {
          display: table !important;
          max-height: none !important;
        }

        .reverse {
          display: table;
          width: 100%;
        }

        .reverse .column.first {
          display: table-footer-group !important;
        }

        .reverse .column.last {
          display: table-header-group !important;
        }

        .row-3 td.column.first .border,
        .row-3 td.column.last .border {
          padding: 5px 20px;
          border-top: 0;
          border-right: 0px;
          border-bottom: 0;
          border-left: 0;
        }

        .row-1 .column-1 .block-5.image_block td.pad {
          padding: 25px 0 0 !important;
        }
      }
    </style>
  </head>

  <body
    style="
      background-color: #000;
      margin: 0;
      padding: 0;
      -webkit-text-size-adjust: none;
      text-size-adjust: none;
    "
  >
<p>Hola $receiver_name estás invitad$gender_casing_single a SAIACONF !!!</p>

    <table
      class="nl-container"
      width="100%"
      border="0"
      cellpadding="0"
      cellspacing="0"
      role="presentation"
      style="
        mso-table-lspace: 0pt;
        mso-table-rspace: 0pt;
        background-color: #000;
      "
    >
      <tbody>
        <tr>
          <td>
            <table
              class="row row-1"
              align="center"
              width="100%"
              border="0"
              cellpadding="0"
              cellspacing="0"
              role="presentation"
              style="
                mso-table-lspace: 0pt;
                mso-table-rspace: 0pt;
                background-color: #000000;
                background-size: auto;
              "
            >
              <tbody>
                <tr>
                  <td>
                    <table
                      class="row-content stack"
                      align="center"
                      border="0"
                      cellpadding="0"
                      cellspacing="0"
                      role="presentation"
                      style="
                        mso-table-lspace: 0pt;
                        mso-table-rspace: 0pt;
                        background-size: auto;
                        background-color: #000;
                        color: #000;
                        width: 650px;
                        margin: 0 auto;
                      "
                      width="650"
                    >
                      <tbody>
                        <tr>
                          <td
                            class="column column-1"
                            width="100%"
                            style="
                              mso-table-lspace: 0pt;
                              mso-table-rspace: 0pt;
                              font-weight: 400;
                              text-align: left;
                              padding-bottom: 5px;
                              padding-top: 5px;
                              vertical-align: top;
                              border-top: 0px;
                              border-right: 0px;
                              border-bottom: 0px;
                              border-left: 0px;
                            "
                          >
                            <table
                              class="image_block block-1"
                              width="100%"
                              border="0"
                              cellpadding="0"
                              cellspacing="0"
                              role="presentation"
                              style="
                                mso-table-lspace: 0pt;
                                mso-table-rspace: 0pt;
                              "
                            >
                              <tr>
                                <td
                                  class="pad"
                                  style="
                                    padding-bottom: 30px;
                                    padding-top: 10px;
                                    width: 100%;
                                  "
                                >
                                  <div
                                    class="alignment"
                                    align="center"
                                    style="line-height: 10px"
                                  >
                                    <a
                                      href="http://saia.ar"
                                      target="_blank"
                                      style="outline: none"
                                      tabindex="-1"
                                      ><img
                                        src="https://assets.saia.ar/saia/circulo-blanco-saia.png"
                                        style="
                                          display: block;
                                          height: auto;
                                          margin-top: 5em;
                                          border: 0;
                                          max-width: 80px;
                                          width: 100%;
                                        "
                                        width="167"
                                        alt="Your Logo"
                                        title="Your Logo"
                                    /></a>
                                  </div>
                                </td>
                              </tr>
                            </table>
                            <table
                              class="heading_block block-2"
                              width="100%"
                              border="0"
                              cellpadding="0"
                              cellspacing="0"
                              role="presentation"
                              style="
                                mso-table-lspace: 0pt;
                                mso-table-rspace: 0pt;
                              "
                            >
                              <tr>
                                <td
                                  class="pad"
                                  style="
                                    padding-bottom: 5px;
                                    text-align: center;
                                    width: 100%;
                                  "
                                >
                                  <h1
                                    style="
                                      margin: 0;
                                      color: #ffffff;
                                      direction: ltr;
                                      font-family: 'Manrope', Helvetica Neue,
                                        Helvetica, Arial, sans-serif;
                                      font-size: 56px;
                                      font-weight: 700;
                                      letter-spacing: normal;
                                      line-height: 120%;
                                      text-align: center;
                                      margin-top: 0;
                                      margin-bottom: 0;
                                    "
                                  >
                                    $receiver_name
                                  </h1>
                                </td>
                              </tr>
                            </table>
                            <table
                              class="paragraph_block block-3"
                              width="100%"
                              border="0"
                              cellpadding="0"
                              cellspacing="0"
                              role="presentation"
                              style="
                                mso-table-lspace: 0pt;
                                mso-table-rspace: 0pt;
                                word-break: break-word;
                              "
                            >
                              <tr>
                                <td class="pad" style="padding-bottom: 20px">
                                  <div
                                    style="
                                      color: #ffffff;
                                      direction: ltr;
                                      font-family: 'Manrope', Helvetica Neue,
                                        Helvetica, Arial, sans-serif;
                                      font-size: 16px;
                                      font-weight: 400;
                                      letter-spacing: 0px;
                                      line-height: 150%;
                                      text-align: center;
                                      mso-line-height-alt: 24px;
                                    "
                                  >
                                    <p style="margin: 0">$gender_casing_single</p>
                                  </div>
                                </td>
                              </tr>
                            </table>
                            <table
                              class="button_block block-4"
                              width="100%"
                              border="0"
                              cellpadding="0"
                              cellspacing="0"
                              role="presentation"
                              style="
                                mso-table-lspace: 0pt;
                                mso-table-rspace: 0pt;
                              "
                            >
                              <tr>
                                <td
                                  class="pad"
                                  style="
                                    padding-bottom: 15px;
                                    text-align: center;
                                  "
                                >
                                  <div class="alignment" align="center">
                                    <!--[if mso]><v:roundrect xmlns:v="urn:schemas-microsoft-com:vml" xmlns:w="urn:schemas-microsoft-com:office:word" href="http://saia.ar" style="height:52px;width:196px;v-text-anchor:middle;" arcsize="0%" stroke="false" fillcolor="#ffffff"><w:anchorlock/><v:textbox inset="0px,0px,0px,0px"><center style="color:#000000; font-family:Arial, sans-serif; font-size:16px"><![endif]-->
                                    <h3
                                      style="
                                        margin: 0;
                                        color: #ffffff;
                                        direction: ltr;
                                        font-family: 'Manrope', Helvetica Neue,
                                          Helvetica, Arial, sans-serif;
                                        font-size: 36px;
                                        font-weight: 800;
                                        letter-spacing: normal;
                                        line-height: 120%;
                                        text-align: center;
                                        margin-top: 0;
                                        margin-bottom: 0;
                                      "
                                    >
                                    </h3>

                                    <!--[if mso]></center></v:textbox></v:roundrect><![endif]-->
                                  </div>
                                </td>
                              </tr>
                            </table>
                            <table
                              class="image_block block-5"
                              width="100%"
                              border="0"
                              cellpadding="0"
                              cellspacing="0"
                              role="presentation"
                              style="
                                mso-table-lspace: 0pt;
                                mso-table-rspace: 0pt;
                              "
                            >
                              <tr>
                                <td
                                  class="pad"
                                  style="
                                    padding-top: 5px;
                                    padding-bottom: 90px;
                                    width: 100%;
                                    padding-right: 0px;
                                    padding-left: 0px;
                                  "
                                >
                                  <div
                                    class="alignment"
                                    align="center"
                                    style="line-height: 10px"
                                  >
                                    <!-- <img
                                      class="fullWidth"
                                      src="https://assets.saia.ar/saia/pics/sede-saia-futurista.png"
                                      style="
                                        display: block;
                                        height: auto;
                                        border: 0;
                                        max-width: 200px;
                                        width: 100%;
                                      "
                                      width="200"
                                      alt="Laptop"
                                      title="Laptop"
                                    /> -->
                                  </div>
                                </td>
                              </tr>
                            </table>
                          </td>
                        </tr>
                      </tbody>
                    </table>
                  </td>
                </tr>
              </tbody>
            </table>
            <table
              class="row row-2"
              align="center"
              width="100%"
              border="0"
              cellpadding="0"
              cellspacing="0"
              role="presentation"
              style="
                mso-table-lspace: 0pt;
                mso-table-rspace: 0pt;
                background-size: auto;
              "
            >
              <tbody>
                <tr>
                  <td>
                    <table
                      class="row-content stack"
                      align="center"
                      border="0"
                      cellpadding="0"
                      cellspacing="0"
                      role="presentation"
                      style="
                        mso-table-lspace: 0pt;
                        mso-table-rspace: 0pt;
                        background-size: auto;
                        background-color: #000;
                        border-radius: 0;
                        color: #000;
                        width: 650px;
                        margin: 0 auto;
                      "
                      width="650"
                    >
                      <tbody>
                        <tr>
                          <td
                            class="column column-1"
                            width="50%"
                            style="
                              mso-table-lspace: 0pt;
                              mso-table-rspace: 0pt;
                              font-weight: 400;
                              text-align: left;
                              padding-bottom: 5px;
                              padding-left: 20px;
                              padding-right: 20px;
                              padding-top: 5px;
                              vertical-align: top;
                              border-top: 0px;
                              border-right: 0px;
                              border-bottom: 0px;
                              border-left: 0px;
                            "
                          >
                            <table
                              class="image_block block-1"
                              width="100%"
                              border="0"
                              cellpadding="0"
                              cellspacing="0"
                              role="presentation"
                              style="
                                mso-table-lspace: 0pt;
                                mso-table-rspace: 0pt;
                              "
                            >
                              <tr>
                                <td class="pad" style="width: 100%">
                                  <div
                                    class="alignment"
                                    align="center"
                                    style="line-height: 10px"
                                  >
                                    <img
                                      src="https://assets.saia.ar/saia/pics/sede-futurista-2.png"
                                      style="
                                        display: block;
                                        height: auto;
                                        border: 0;
                                        max-width: 285px;
                                        width: 100%;
                                      "
                                      width="285"
                                      alt="Facebook"
                                      title="Facebook"
                                    />
                                  </div>
                                </td>
                              </tr>
                            </table>
                          </td>
                          <td
                            class="column column-2"
                            width="50%"
                            style="
                              mso-table-lspace: 0pt;
                              mso-table-rspace: 0pt;
                              font-weight: 400;
                              text-align: left;
                              padding-bottom: 5px;
                              padding-left: 20px;
                              padding-right: 20px;
                              padding-top: 5px;
                              vertical-align: top;
                              border-top: 0px;
                              border-right: 0px;
                              border-bottom: 0px;
                              border-left: 0px;
                            "
                          >
                            <table
                              class="social_block block-1"
                              width="100%"
                              border="0"
                              cellpadding="0"
                              cellspacing="0"
                              role="presentation"
                              style="
                                mso-table-lspace: 0pt;
                                mso-table-rspace: 0pt;
                              "
                            >
                              <tr>
                                <td
                                  class="pad"
                                  style="
                                    text-align: left;
                                    padding-right: 0px;
                                    padding-left: 0px;
                                  "
                                >
                                  <div class="alignment" align="left">
                                    <table
                                      class="social-table"
                                      width="36px"
                                      border="0"
                                      cellpadding="0"
                                      cellspacing="0"
                                      role="presentation"
                                      style="
                                        mso-table-lspace: 0pt;
                                        mso-table-rspace: 0pt;
                                        display: inline-block;
                                      "
                                    >
                                      <tr>
                                        <td style="padding: 0 4px 0 0">
                                          <a
                                            href="https://chat.whatsapp.com/LTENHK64nzDAc7vqQxcEef"
                                            target="_blank"
                                            ><img
                                              src="https://app-rsrc.getbee.io/public/resources/social-networks-icon-sets/t-only-logo-white/whatsapp@2x.png"
                                              width="32"
                                              height="32"
                                              alt="Facebook"
                                              title="facebook"
                                              style="
                                                display: block;
                                                height: auto;
                                                border: 0;
                                              "
                                          /></a>
                                        </td>
                                      </tr>
                                    </table>
                                  </div>
                                </td>
                              </tr>
                            </table>
                            <table
                              class="heading_block block-2"
                              width="100%"
                              border="0"
                              cellpadding="0"
                              cellspacing="0"
                              role="presentation"
                              style="
                                mso-table-lspace: 0pt;
                                mso-table-rspace: 0pt;
                              "
                            >
                              <tr>
                                <td
                                  class="pad"
                                  style="text-align: center; width: 100%"
                                >
                                  <h1
                                    style="
                                      margin: 0;
                                      color: #ffffff;
                                      direction: ltr;
                                      font-family: 'Manrope', Helvetica Neue,
                                        Helvetica, Arial, sans-serif;
                                      font-size: 38px;
                                      font-weight: 700;
                                      letter-spacing: normal;
                                      line-height: 120%;
                                      text-align: left;
                                      margin-top: 0;
                                      margin-bottom: 0;
                                    "
                                  >
                                    <span class="tinyMce-placeholder"
                                      >Nuestra comunidad en WhatsApp
                                    </span>
                                  </h1>
                                </td>
                              </tr>
                            </table>
                            <table
                              class="paragraph_block block-3"
                              width="100%"
                              border="0"
                              cellpadding="0"
                              cellspacing="0"
                              role="presentation"
                              style="
                                mso-table-lspace: 0pt;
                                mso-table-rspace: 0pt;
                                word-break: break-word;
                              "
                            >
                              <tr>
                                <td class="pad" style="padding-bottom: 20px">
                                  <div
                                    style="
                                      color: #ffffff;
                                      direction: ltr;
                                      font-family: 'Manrope', Helvetica Neue,
                                        Helvetica, Arial, sans-serif;
                                      font-size: 16px;
                                      font-weight: 400;
                                      letter-spacing: 0px;
                                      line-height: 150%;
                                      text-align: left;
                                      mso-line-height-alt: 24px;
                                    "
                                  >
                                    <p style="margin: 0">
                                      Los líderes de cada grupo van a recibir tu
                                      perfil de acuerdo a la información que
                                      colocaste en el formulario y te van a
                                      agregar al grupo correspondiente.<br />
                                      Pero primero tenés que estar en la
                                      comunidad.<br />
                                      Hacé click en el botón y sumate a nuestra
                                      comunidad en WhatsApp.
                                    </p>
                                  </div>
                                </td>
                              </tr>
                            </table>
                            <table
                              class="button_block block-4"
                              width="100%"
                              border="0"
                              cellpadding="0"
                              cellspacing="0"
                              role="presentation"
                              style="
                                mso-table-lspace: 0pt;
                                mso-table-rspace: 0pt;
                              "
                            >
                              <tr>
                                <td class="pad" style="text-align: left">
                                  <div class="alignment" align="left">
                                    <!--[if mso]><v:roundrect xmlns:v="urn:schemas-microsoft-com:vml" xmlns:w="urn:schemas-microsoft-com:office:word" href="http://saia.ar" style="height:52px;width:117px;v-text-anchor:middle;" arcsize="0%" stroke="false" fillcolor="#ffffff"><w:anchorlock/><v:textbox inset="0px,0px,0px,0px"><center style="color:#000000; font-family:Arial, sans-serif; font-size:16px"><!
                                    [endif]--><a
                                      href="https://chat.whatsapp.com/LTENHK64nzDAc7vqQxcEef"
                                      target="_blank"
                                      style="
                                        text-decoration: none;
                                        display: inline-block;
                                        color: #000000;
                                        background-color: #ffffff;
                                        border-radius: 0px;
                                        width: auto;
                                        border-top: 0px solid transparent;
                                        font-weight: 400;
                                        border-right: 0px solid transparent;
                                        border-bottom: 0px solid transparent;
                                        border-left: 0px solid transparent;
                                        padding-top: 10px;
                                        padding-bottom: 10px;
                                        font-family: 'Manrope', Helvetica Neue,
                                          Helvetica, Arial, sans-serif;
                                        font-size: 16px;
                                        text-align: center;
                                        mso-border-alt: none;
                                        word-break: keep-all;
                                      "
                                      ><span
                                        style="
                                          padding-left: 25px;
                                          padding-right: 25px;
                                          font-size: 16px;
                                          display: inline-block;
                                          letter-spacing: normal;
                                        "
                                        ><span
                                          style="
                                            word-break: break-word;
                                            line-height: 32px;
                                          "
                                          >Sumate</span
                                        ></span
                                      ></a
                                    >><!--[if mso]></center></v:textbox></v:roundrect><![endif]-->
                                  </div>
                                </td>
                              </tr>
                            </table>
                          </td>
                        </tr>
                      </tbody>
                    </table>
                  </td>
                </tr>
              </tbody>
            </table>
            <table
              class="row row-3"
              align="center"
              width="100%"
              border="0"
              cellpadding="0"
              cellspacing="0"
              role="presentation"
              style="
                mso-table-lspace: 0pt;
                mso-table-rspace: 0pt;
                background-size: auto;
              "
            >
              <tbody>
                <tr>
                  <td>
                    <table
                      class="row-content stack"
                      align="center"
                      border="0"
                      cellpadding="0"
                      cellspacing="0"
                      role="presentation"
                      style="
                        mso-table-lspace: 0pt;
                        mso-table-rspace: 0pt;
                        background-size: auto;
                        background-color: #000;
                        border-radius: 0;
                        color: #000;
                        width: 650px;
                        margin: 0 auto;
                      "
                      width="650"
                    >
                      <tbody>
                        <tr class="reverse">
                          <td
                            class="column column-1 first"
                            width="50%"
                            style="
                              mso-table-lspace: 0pt;
                              mso-table-rspace: 0pt;
                              font-weight: 400;
                              text-align: left;
                              padding-bottom: 5px;
                              padding-left: 20px;
                              padding-right: 20px;
                              padding-top: 5px;
                              vertical-align: top;
                              border-top: 0px;
                              border-right: 0px;
                              border-bottom: 0px;
                              border-left: 0px;
                            "
                          >
                            <div class="border">
                              <table
                                class="social_block block-1"
                                width="100%"
                                border="0"
                                cellpadding="0"
                                cellspacing="0"
                                role="presentation"
                                style="
                                  mso-table-lspace: 0pt;
                                  mso-table-rspace: 0pt;
                                "
                              >
                                <tr>
                                  <td
                                    class="pad"
                                    style="
                                      text-align: left;
                                      padding-right: 0px;
                                      padding-left: 0px;
                                    "
                                  >
                                    <div class="alignment" align="left">
                                      <table
                                        class="social-table"
                                        width="36px"
                                        border="0"
                                        cellpadding="0"
                                        cellspacing="0"
                                        role="presentation"
                                        style="
                                          mso-table-lspace: 0pt;
                                          mso-table-rspace: 0pt;
                                          display: inline-block;
                                        "
                                      >
                                        <tr>
                                          <td style="padding: 0 4px 0 0">
                                            <a
                                              href="https://www.instagram.com"
                                              target="_blank"
                                              ><img
                                                src="https://app-rsrc.getbee.io/public/resources/social-networks-icon-sets/t-only-logo-white/instagram@2x.png"
                                                width="32"
                                                height="32"
                                                alt="Instagram"
                                                title="Instagram"
                                                style="
                                                  display: block;
                                                  height: auto;
                                                  border: 0;
                                                "
                                            /></a>
                                          </td>
                                        </tr>
                                      </table>
                                    </div>
                                  </td>
                                </tr>
                              </table>
                              <table
                                class="heading_block block-2"
                                width="100%"
                                border="0"
                                cellpadding="0"
                                cellspacing="0"
                                role="presentation"
                                style="
                                  mso-table-lspace: 0pt;
                                  mso-table-rspace: 0pt;
                                "
                              >
                                <tr>
                                  <td
                                    class="pad"
                                    style="text-align: center; width: 100%"
                                  >
                                    <h1
                                      style="
                                        margin: 0;
                                        color: #ffffff;
                                        direction: ltr;
                                        font-family: 'Manrope', Helvetica Neue,
                                          Helvetica, Arial, sans-serif;
                                        font-size: 38px;
                                        font-weight: 700;
                                        letter-spacing: normal;
                                        line-height: 120%;
                                        text-align: left;
                                        margin-top: 0;
                                        margin-bottom: 0;
                                      "
                                    >
                                      <span class="tinyMce-placeholder"
                                        >Estamos en Instagram</span
                                      >
                                    </h1>
                                  </td>
                                </tr>
                              </table>
                              <table
                                class="paragraph_block block-3"
                                width="100%"
                                border="0"
                                cellpadding="0"
                                cellspacing="0"
                                role="presentation"
                                style="
                                  mso-table-lspace: 0pt;
                                  mso-table-rspace: 0pt;
                                  word-break: break-word;
                                "
                              >
                                <tr>
                                  <td class="pad" style="padding-bottom: 20px">
                                    <div
                                      style="
                                        color: #ffffff;
                                        direction: ltr;
                                        font-family: 'Manrope', Helvetica Neue,
                                          Helvetica, Arial, sans-serif;
                                        font-size: 16px;
                                        font-weight: 400;
                                        letter-spacing: 0px;
                                        line-height: 150%;
                                        text-align: left;
                                        mso-line-height-alt: 24px;
                                      "
                                    >
                                      <p style="margin: 0">
                                        Para estar al tanto de nuestros eventos
                                        y charlas.
                                      </p>
                                    </div>
                                  </td>
                                </tr>
                              </table>
                              <table
                                class="button_block block-4"
                                width="100%"
                                border="0"
                                cellpadding="0"
                                cellspacing="0"
                                role="presentation"
                                style="
                                  mso-table-lspace: 0pt;
                                  mso-table-rspace: 0pt;
                                "
                              >
                                <tr>
                                  <td class="pad" style="text-align: left">
                                    <div class="alignment" align="left">
                                      <!--[if mso]><v:roundrect xmlns:v="urn:schemas-microsoft-com:vml" xmlns:w="urn:schemas-microsoft-com:office:word" href="http://saia.ar" style="height:52px;width:117px;v-text-anchor:middle;" arcsize="0%" stroke="false" fillcolor="#ffffff"><w:anchorlock/><v:textbox inset="0px,0px,0px,0px"><center style="color:#000000; font-family:Arial, sans-serif; font-size:16px"><!
                                      [endif]--><a
                                        href="https://www.instagram.com/saia_ar/"
                                        target="_blank"
                                        style="
                                          text-decoration: none;
                                          display: inline-block;
                                          color: #000000;
                                          background-color: #ffffff;
                                          border-radius: 0px;
                                          width: auto;
                                          border-top: 0px solid transparent;
                                          font-weight: 400;
                                          border-right: 0px solid transparent;
                                          border-bottom: 0px solid transparent;
                                          border-left: 0px solid transparent;
                                          padding-top: 10px;
                                          padding-bottom: 10px;
                                          font-family: 'Manrope', Helvetica Neue,
                                            Helvetica, Arial, sans-serif;
                                          font-size: 16px;
                                          text-align: center;
                                          mso-border-alt: none;
                                          word-break: keep-all;
                                        "
                                        ><span
                                          style="
                                            padding-left: 25px;
                                            padding-right: 25px;
                                            font-size: 16px;
                                            display: inline-block;
                                            letter-spacing: normal;
                                          "
                                          ><span
                                            style="
                                              word-break: break-word;
                                              line-height: 32px;
                                            "
                                            >Seguinos</span
                                          ></span
                                        ></a
                                      >><!--[if mso]></center></v:textbox></v:roundrect><![endif]-->
                                    </div>
                                  </td>
                                </tr>
                              </table>
                            </div>
                          </td>
                          <td
                            class="column column-2 last"
                            width="50%"
                            style="
                              mso-table-lspace: 0pt;
                              mso-table-rspace: 0pt;
                              font-weight: 400;
                              text-align: left;
                              padding-bottom: 5px;
                              padding-left: 20px;
                              padding-right: 20px;
                              padding-top: 5px;
                              vertical-align: top;
                              border-top: 0px;
                              border-right: 0px;
                              border-bottom: 0px;
                              border-left: 0px;
                            "
                          >
                            <div class="border">
                              <table
                                class="image_block block-1"
                                width="100%"
                                border="0"
                                cellpadding="0"
                                cellspacing="0"
                                role="presentation"
                                style="
                                  mso-table-lspace: 0pt;
                                  mso-table-rspace: 0pt;
                                "
                              >
                                <tr>
                                  <td class="pad" style="width: 100%">
                                    <div
                                      class="alignment"
                                      align="center"
                                      style="line-height: 10px"
                                    >
                                      <img
                                        src="https://assets.saia.ar/saia/pics/instagram-screenshot-wide-min.jpg"
                                        style="
                                          display: block;
                                          height: auto;
                                          border: 0;
                                          max-width: 285px;
                                          width: 100%;
                                        "
                                        width="285"
                                        alt="Instagram"
                                        title="Instagram"
                                      />
                                    </div>
                                  </td>
                                </tr>
                              </table>
                            </div>
                          </td>
                        </tr>
                      </tbody>
                    </table>
                  </td>
                </tr>
              </tbody>
            </table>
            <table
              class="row row-4"
              align="center"
              width="100%"
              border="0"
              cellpadding="0"
              cellspacing="0"
              role="presentation"
              style="mso-table-lspace: 0pt; mso-table-rspace: 0pt"
            >
              <tbody>
                <tr>
                  <td>
                    <table
                      class="row-content stack"
                      align="center"
                      border="0"
                      cellpadding="0"
                      cellspacing="0"
                      role="presentation"
                      style="
                        mso-table-lspace: 0pt;
                        mso-table-rspace: 0pt;
                        background-color: #000;
                        border-radius: 0;
                        color: #000;
                        width: 650px;
                        margin: 0 auto;
                      "
                      width="650"
                    >
                      <tbody>
                        <tr>
                          <td
                            class="column column-1"
                            width="50%"
                            style="
                              mso-table-lspace: 0pt;
                              mso-table-rspace: 0pt;
                              font-weight: 400;
                              text-align: left;
                              padding-bottom: 5px;
                              padding-left: 20px;
                              padding-right: 20px;
                              padding-top: 5px;
                              vertical-align: top;
                              border-top: 0px;
                              border-right: 0px;
                              border-bottom: 0px;
                              border-left: 0px;
                            "
                          >
                            <table
                              class="image_block block-1"
                              width="100%"
                              border="0"
                              cellpadding="0"
                              cellspacing="0"
                              role="presentation"
                              style="
                                mso-table-lspace: 0pt;
                                mso-table-rspace: 0pt;
                              "
                            >
                              <tr>
                                <td class="pad" style="width: 100%">
                                  <div
                                    class="alignment"
                                    align="center"
                                    style="line-height: 10px"
                                  >
                                    <img
                                      src="https://assets.saia.ar/saia/pics/youtube-channel-screenshot.png"
                                      style="
                                        display: block;
                                        height: auto;
                                        border: 0;
                                        max-width: 285px;
                                        width: 100%;
                                      "
                                      width="285"
                                      alt="LinkedIn"
                                      title="LinkedIn"
                                    />
                                  </div>
                                </td>
                              </tr>
                            </table>
                          </td>
                          <td
                            class="column column-2"
                            width="50%"
                            style="
                              mso-table-lspace: 0pt;
                              mso-table-rspace: 0pt;
                              font-weight: 400;
                              text-align: left;
                              padding-bottom: 5px;
                              padding-left: 20px;
                              padding-right: 20px;
                              padding-top: 5px;
                              vertical-align: top;
                              border-top: 0px;
                              border-right: 0px;
                              border-bottom: 0px;
                              border-left: 0px;
                            "
                          >
                            <table
                              class="social_block block-1"
                              width="100%"
                              border="0"
                              cellpadding="0"
                              cellspacing="0"
                              role="presentation"
                              style="
                                mso-table-lspace: 0pt;
                                mso-table-rspace: 0pt;
                              "
                            >
                              <tr>
                                <td
                                  class="pad"
                                  style="
                                    text-align: left;
                                    padding-right: 0px;
                                    padding-left: 0px;
                                  "
                                >
                                  <div class="alignment" align="left">
                                    <table
                                      class="social-table"
                                      width="36px"
                                      border="0"
                                      cellpadding="0"
                                      cellspacing="0"
                                      role="presentation"
                                      style="
                                        mso-table-lspace: 0pt;
                                        mso-table-rspace: 0pt;
                                        display: inline-block;
                                      "
                                    >
                                      <tr>
                                        <td style="padding: 0 4px 0 0">
                                          <a
                                            href="https://www.youtube.com/@saia_ar/streams"
                                            target="_blank"
                                            ><img
                                              src="https://app-rsrc.getbee.io/public/resources/social-networks-icon-sets/t-only-logo-white/youtube@2x.png"
                                              width="32"
                                              height="32"
                                              alt="Youtube Live SAIA"
                                              title="Youtube Live SAIA"
                                              style="
                                                display: block;
                                                height: auto;
                                                border: 0;
                                              "
                                          /></a>
                                        </td>
                                      </tr>
                                    </table>
                                  </div>
                                </td>
                              </tr>
                            </table>
                            <table
                              class="heading_block block-2"
                              width="100%"
                              border="0"
                              cellpadding="0"
                              cellspacing="0"
                              role="presentation"
                              style="
                                mso-table-lspace: 0pt;
                                mso-table-rspace: 0pt;
                              "
                            >
                              <tr>
                                <td
                                  class="pad"
                                  style="text-align: center; width: 100%"
                                >
                                  <h1
                                    style="
                                      margin: 0;
                                      color: #ffffff;
                                      direction: ltr;
                                      font-family: 'Manrope', Helvetica Neue,
                                        Helvetica, Arial, sans-serif;
                                      font-size: 38px;
                                      font-weight: 700;
                                      letter-spacing: normal;
                                      line-height: 120%;
                                      text-align: left;
                                      margin-top: 0;
                                      margin-bottom: 0;
                                    "
                                  >
                                    <span class="tinyMce-placeholder"
                                      >Transmitimos por YouTube Live</span
                                    >
                                  </h1>
                                </td>
                              </tr>
                            </table>
                            <table
                              class="paragraph_block block-3"
                              width="100%"
                              border="0"
                              cellpadding="0"
                              cellspacing="0"
                              role="presentation"
                              style="
                                mso-table-lspace: 0pt;
                                mso-table-rspace: 0pt;
                                word-break: break-word;
                              "
                            >
                              <tr>
                                <td class="pad" style="padding-bottom: 20px">
                                  <div
                                    style="
                                      color: #ffffff;
                                      direction: ltr;
                                      font-family: 'Manrope', Helvetica Neue,
                                        Helvetica, Arial, sans-serif;
                                      font-size: 16px;
                                      font-weight: 400;
                                      letter-spacing: 0px;
                                      line-height: 150%;
                                      text-align: left;
                                      mso-line-height-alt: 24px;
                                    "
                                  >
                                    <p style="margin: 0">
                                      Buscá los eventos publicados, si no podés
                                      estár en el vivo podés ver los videos en
                                      nuestro canal.
                                    </p>
                                  </div>
                                </td>
                              </tr>
                            </table>
                            <table
                              class="button_block block-4"
                              width="100%"
                              border="0"
                              cellpadding="0"
                              cellspacing="0"
                              role="presentation"
                              style="
                                mso-table-lspace: 0pt;
                                mso-table-rspace: 0pt;
                              "
                            >
                              <tr>
                                <td class="pad" style="text-align: left">
                                  <div class="alignment" align="left">
                                    <!--[if mso]><v:roundrect xmlns:v="urn:schemas-microsoft-com:vml" xmlns:w="urn:schemas-microsoft-com:office:word" href="http://saia.ar" style="height:52px;width:117px;v-text-anchor:middle;" arcsize="0%" stroke="false" fillcolor="#ffffff"><w:anchorlock/><v:textbox inset="0px,0px,0px,0px"><center style="color:#000000; font-family:Arial, sans-serif; font-size:16px"><!
                                    [endif]--><a
                                      href="https://www.youtube.com/@saia_ar/streams"
                                      target="_blank"
                                      style="
                                        text-decoration: none;
                                        display: inline-block;
                                        color: #000000;
                                        background-color: #ffffff;
                                        border-radius: 0px;
                                        width: auto;
                                        border-top: 0px solid transparent;
                                        font-weight: 400;
                                        border-right: 0px solid transparent;
                                        border-bottom: 0px solid transparent;
                                        border-left: 0px solid transparent;
                                        padding-top: 10px;
                                        padding-bottom: 10px;
                                        font-family: 'Manrope', Helvetica Neue,
                                          Helvetica, Arial, sans-serif;
                                        font-size: 16px;
                                        text-align: center;
                                        mso-border-alt: none;
                                        word-break: keep-all;
                                      "
                                      ><span
                                        style="
                                          padding-left: 25px;
                                          padding-right: 25px;
                                          font-size: 16px;
                                          display: inline-block;
                                          letter-spacing: normal;
                                        "
                                        ><span
                                          style="
                                            word-break: break-word;
                                            line-height: 32px;
                                          "
                                          >Subscribite</span
                                        ></span
                                      ></a
                                    >><!--[if mso]></center></v:textbox></v:roundrect><![endif]-->
                                  </div>
                                </td>
                              </tr>
                            </table>
                          </td>
                        </tr>
                      </tbody>
                    </table>
                  </td>
                </tr>
              </tbody>
            </table>
            <table
              class="row row-5"
              align="center"
              width="100%"
              border="0"
              cellpadding="0"
              cellspacing="0"
              role="presentation"
              style="mso-table-lspace: 0pt; mso-table-rspace: 0pt"
            >
              <tbody>
                <tr>
                  <td>
                    <table
                      class="row-content stack"
                      align="center"
                      border="0"
                      cellpadding="0"
                      cellspacing="0"
                      role="presentation"
                      style="
                        mso-table-lspace: 0pt;
                        mso-table-rspace: 0pt;
                        background-color: #000;
                        border-radius: 0;
                        color: #000;
                        width: 650px;
                        margin: 0 auto;
                      "
                      width="650"
                    >
                      <tbody>
                        <tr>
                          <td
                            class="column column-1"
                            width="100%"
                            style="
                              mso-table-lspace: 0pt;
                              mso-table-rspace: 0pt;
                              font-weight: 400;
                              text-align: left;
                              padding-bottom: 5px;
                              padding-top: 5px;
                              vertical-align: top;
                              border-top: 0px;
                              border-right: 0px;
                              border-bottom: 0px;
                              border-left: 0px;
                            "
                          >
                            <div
                              class="spacer_block block-1"
                              style="
                                height: 35px;
                                line-height: 35px;
                                font-size: 1px;
                              "
                            >
                              &#8202;
                            </div>
                          </td>
                        </tr>
                      </tbody>
                    </table>
                  </td>
                </tr>
              </tbody>
            </table>
            <table
              class="row row-6"
              align="center"
              width="100%"
              border="0"
              cellpadding="0"
              cellspacing="0"
              role="presentation"
              style="mso-table-lspace: 0pt; mso-table-rspace: 0pt"
            >
              <tbody>
                <tr>
                  <td>
                    <table
                      class="row-content stack"
                      align="center"
                      border="0"
                      cellpadding="0"
                      cellspacing="0"
                      role="presentation"
                      style="
                        mso-table-lspace: 0pt;
                        mso-table-rspace: 0pt;
                        background-color: #000;
                        border-radius: 0;
                        color: #000;
                        width: 650px;
                        margin: 0 auto;
                      "
                      width="650"
                    >
                      <tbody>
                        <tr>
                          <td
                            class="column column-1"
                            width="100%"
                            style="
                              mso-table-lspace: 0pt;
                              mso-table-rspace: 0pt;
                              font-weight: 400;
                              text-align: left;
                              padding-bottom: 5px;
                              padding-top: 5px;
                              vertical-align: top;
                              border-top: 0px;
                              border-right: 0px;
                              border-bottom: 0px;
                              border-left: 0px;
                            "
                          >
                            <table
                              class="social_block block-1"
                              width="100%"
                              border="0"
                              cellpadding="0"
                              cellspacing="0"
                              role="presentation"
                              style="
                                mso-table-lspace: 0pt;
                                mso-table-rspace: 0pt;
                              "
                            >
                              <tr>
                                <td
                                  class="pad"
                                  style="
                                    text-align: center;
                                    padding-right: 0px;
                                    padding-left: 0px;
                                  "
                                >
                                  <div class="alignment" align="center">
                                    <table
                                      class="social-table"
                                      width="108px"
                                      border="0"
                                      cellpadding="0"
                                      cellspacing="0"
                                      role="presentation"
                                      style="
                                        mso-table-lspace: 0pt;
                                        mso-table-rspace: 0pt;
                                        display: inline-block;
                                      "
                                    >
                                      <tr>
                                        <td style="padding: 0 2px 0 2px">
                                          <a
                                            href="https://www.facebook.com/profile.php?id=100090704183099"
                                            target="_blank"
                                            ><img
                                              src="https://app-rsrc.getbee.io/public/resources/social-networks-icon-sets/t-only-logo-white/facebook@2x.png"
                                              width="32"
                                              height="32"
                                              alt="Facebook"
                                              title="facebook"
                                              style="
                                                display: block;
                                                height: auto;
                                                border: 0;
                                              "
                                          /></a>
                                        </td>
                                        <td style="padding: 0 2px 0 2px">
                                          <a
                                            href="https://twitter.com/SAIA_AR"
                                            target="_blank"
                                            ><img
                                              src="https://app-rsrc.getbee.io/public/resources/social-networks-icon-sets/t-only-logo-white/twitter@2x.png"
                                              width="32"
                                              height="32"
                                              alt="Linkedin"
                                              title="linkedin"
                                              style="
                                                display: block;
                                                height: auto;
                                                border: 0;
                                              "
                                          /></a>
                                        </td>
                                        <td style="padding: 0 2px 0 2px">
                                          <a
                                            href="https://www.linkedin.com/company/sociedad-argentina-de-inteligencia-artificial/?viewAsMember=true"
                                            target="_blank"
                                            ><img
                                              src="https://app-rsrc.getbee.io/public/resources/social-networks-icon-sets/t-only-logo-white/linkedin@2x.png"
                                              width="32"
                                              height="32"
                                              alt="Instagram"
                                              title="instagram"
                                              style="
                                                display: block;
                                                height: auto;
                                                border: 0;
                                              "
                                          /></a>
                                        </td>
                                      </tr>
                                    </table>
                                  </div>
                                </td>
                              </tr>
                            </table>
                            <table
                              class="paragraph_block block-2"
                              width="100%"
                              border="0"
                              cellpadding="0"
                              cellspacing="0"
                              role="presentation"
                              style="
                                mso-table-lspace: 0pt;
                                mso-table-rspace: 0pt;
                                word-break: break-word;
                              "
                            >
                              <tr>
                                <td class="pad" style="padding-bottom: 5px">
                                  <div
                                    style="
                                      color: #ffffff;
                                      direction: ltr;
                                      font-family: 'Manrope', Helvetica Neue,
                                        Helvetica, Arial, sans-serif;
                                      font-size: 12px;
                                      font-weight: 200;
                                      letter-spacing: 0px;
                                      line-height: 150%;
                                      text-align: center;
                                      mso-line-height-alt: 24px;
                                    "
                                  >
                                    <p style="margin: 0">
                                      2023 © Todos los derechos reservados.
                                    </p>
                                  </div>
                                </td>
                              </tr>
                            </table>
                            <table
                              class="paragraph_block block-3"
                              width="100%"
                              border="0"
                              cellpadding="0"
                              cellspacing="0"
                              role="presentation"
                              style="
                                mso-table-lspace: 0pt;
                                mso-table-rspace: 0pt;
                                word-break: break-word;
                              "
                            >
                              <tr>
                                <td
                                  class="pad"
                                  style="
                                    padding-bottom: 5px;
                                    padding-left: 20px;
                                    padding-right: 20px;
                                  "
                                >
                                  <div
                                    style="
                                      color: #ffffff;
                                      direction: ltr;
                                      font-family: 'Manrope', Helvetica Neue,
                                        Helvetica, Arial, sans-serif;
                                      font-size: 12px;
                                      font-weight: 400;
                                      letter-spacing: 0px;
                                      line-height: 180%;
                                      text-align: center;
                                      mso-line-height-alt: 21.6px;
                                    "
                                  >
                                    <p style="margin: 0">
                                      <!-- <a
                                        href="http://example.com"
                                        target="_blank"
                                        style="
                                          text-decoration: none;
                                          color: #737172;
                                        "
                                        rel="noopener"
                                        >Unsuscribe</a
                                      > -->
                                    </p>
                                  </div>
                                </td>
                              </tr>
                            </table>
                          </td>
                        </tr>
                      </tbody>
                    </table>
                  </td>
                </tr>
              </tbody>
            </table>
            <table
              class="row row-7"
              align="center"
              width="100%"
              border="0"
              cellpadding="0"
              cellspacing="0"
              role="presentation"
              style="
                mso-table-lspace: 0pt;
                mso-table-rspace: 0pt;
                background-color: #ffffff;
              "
            >
              <tbody>
                <tr>
                  <td>
                    <table
                      class="row-content stack"
                      align="center"
                      border="0"
                      cellpadding="0"
                      cellspacing="0"
                      role="presentation"
                      style="
                        mso-table-lspace: 0pt;
                        mso-table-rspace: 0pt;
                        background-color: #fff;
                        color: #000;
                        width: 650px;
                        margin: 0 auto;
                      "
                      width="650"
                    >
                      <tbody>
                        <tr>
                          <td
                            class="column column-1"
                            width="100%"
                            style="
                              mso-table-lspace: 0pt;
                              mso-table-rspace: 0pt;
                              font-weight: 400;
                              text-align: left;
                              padding-bottom: 5px;
                              padding-top: 5px;
                              vertical-align: top;
                              border-top: 0px;
                              border-right: 0px;
                              border-bottom: 0px;
                              border-left: 0px;
                            "
                          >
                            <table
                              class="icons_block block-1"
                              width="100%"
                              border="0"
                              cellpadding="0"
                              cellspacing="0"
                              role="presentation"
                              style="
                                mso-table-lspace: 0pt;
                                mso-table-rspace: 0pt;
                              "
                            >
                              <tr>
                                <td
                                  class="pad"
                                  style="
                                    vertical-align: middle;
                                    color: #1e0e4b;
                                    font-family: 'Inter', sans-serif;
                                    font-size: 15px;
                                    padding-bottom: 5px;
                                    padding-top: 5px;
                                    text-align: center;
                                  "
                                >
                                  <table
                                    width="100%"
                                    cellpadding="0"
                                    cellspacing="0"
                                    role="presentation"
                                    style="
                                      mso-table-lspace: 0pt;
                                      mso-table-rspace: 0pt;
                                    "
                                  >
                                    <tr>
                                      <td
                                        class="alignment"
                                        style="
                                          vertical-align: middle;
                                          text-align: center;
                                        "
                                      >
                                        <!--[if vml]><table align="left" cellpadding="0" cellspacing="0" role="presentation" style="display:inline-block;padding-left:0px;padding-right:0px;mso-table-lspace: 0pt;mso-table-rspace: 0pt;"><![endif]-->
                                        <!--[if !vml]><!-->
                                        <table
                                          class="icons-inner"
                                          style="
                                            mso-table-lspace: 0pt;
                                            mso-table-rspace: 0pt;
                                            display: inline-block;
                                            margin-right: -4px;
                                            padding-left: 0px;
                                            padding-right: 0px;
                                          "
                                          cellpadding="0"
                                          cellspacing="0"
                                          role="presentation"
                                        >
                                          <!--<![endif]-->
                                          <tr>
                                            <td
                                              style="
                                                vertical-align: middle;
                                                text-align: center;
                                                padding-top: 5px;
                                                padding-bottom: 5px;
                                                padding-left: 5px;
                                                padding-right: 6px;
                                              "
                                            >
                                              <a
                                                href="http://saia.ar/"
                                                target="_blank"
                                                style="text-decoration: none"
                                                ><img
                                                  class="icon"
                                                  alt="SAIA Logo"
                                                  src="https://assets.saia.ar/saia/saia-logo-letras-negro.png"
                                                  height="200"
                                                  width="300"
                                                  align="center"
                                                  style="
                                                    display: block;
                                                    height: auto;
                                                    margin: 25 auto;
                                                    border: 0;
                                                  "
                                              /></a>
                                              <div
                                                style="
                                                  color: #000000;
                                                  direction: ltr;
                                                  font-family: 'Manrope',
                                                    Helvetica Neue, Helvetica,
                                                    Arial, sans-serif;
                                                  font-size: 10px;
                                                  font-weight: 200;
                                                  letter-spacing: 0px;
                                                  line-height: 150%;
                                                  text-align: center;
                                                  mso-line-height-alt: 24px;
                                                "
                                              >
                                                <p style="margin: 20">
                                                  Zavaleta 27 1ro B <br />
                                                  Ciudad Autónoma de Buenos
                                                  Aires <br />
                                                  Argentina <br />
                                                  +54 9 11 6408 1743 <br />
                                                  CUIT 33-71736089-9 <br />
                                                </p>
                                              </div>
                                            </td>
                                            <td
                                              style="
                                                font-family: 'Inter', sans-serif;
                                                font-size: 15px;
                                                color: #1e0e4b;
                                                vertical-align: middle;
                                                letter-spacing: undefined;
                                                text-align: center;
                                              "
                                            >
                                              <a
                                                href="https://saia.ar"
                                                target="_blank"
                                                style="
                                                  color: #1e0e4b;
                                                  text-decoration: none;
                                                "
                                              ></a>
                                            </td>
                                          </tr>
                                        </table>
                                      </td>
                                    </tr>
                                  </table>
                                </td>
                              </tr>
                            </table>
                          </td>
                        </tr>
                      </tbody>
                    </table>
                  </td>
                </tr>
              </tbody>
            </table>
          </td>
        </tr>
      </tbody>
    </table>
    <!-- End -->
  </body>
</html>
"""
)
