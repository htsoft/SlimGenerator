<?php

declare(strict_types=1);

namespace App\Application\Actions\##TABLENAMECAP##;

use Psr\Http\Message\ResponseInterface as Response;

class ##TABLENAMECAP##GetAction extends ##TABLENAMECAP##Action
{
    /**
     * {@inheritdoc}
     */
    protected function action(): Response
    {
        ##KEYSARGS##
        $this->logger->info("Requested record for ##TABLENAMECAP## with keys"##LISTKEYSVALUES##);
        $obj = $this->##TABLENAME##Repository->get(##KEYSPARAMS##);
        return $this->respondWithData($obj);
    }
}