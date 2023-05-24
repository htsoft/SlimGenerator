<?php

declare(strict_types=1);

namespace App\Domain\##TABLENAME##;

use JsonSerializable;

class ##TABLENAME## implements JsonSerializable
{
    ##PROPERTIES##

    public function __construct(##CONSTRUCTORPARAMETERS##)
    {
        ##CONSTRUCTORASSIGNMENTS##
    }

    ##GETTERS##
    
    #[\ReturnTypeWillChange]
    public function jsonSerialize(): array
    {
        return [
            ##JSONFIELDS##
        ];
    }
}
