graph [
  node [
    id 0
    label 1
    disk 1
    cpu 3
    memory 3
  ]
  node [
    id 1
    label 2
    disk 10
    cpu 2
    memory 15
  ]
  node [
    id 2
    label 3
    disk 1
    cpu 1
    memory 12
  ]
  node [
    id 3
    label 4
    disk 7
    cpu 3
    memory 14
  ]
  node [
    id 4
    label 5
    disk 2
    cpu 1
    memory 5
  ]
  node [
    id 5
    label 6
    disk 10
    cpu 4
    memory 13
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 28
    bw 174
  ]
  edge [
    source 0
    target 1
    delay 28
    bw 117
  ]
  edge [
    source 0
    target 2
    delay 31
    bw 133
  ]
  edge [
    source 0
    target 3
    delay 32
    bw 99
  ]
  edge [
    source 1
    target 5
    delay 27
    bw 154
  ]
  edge [
    source 2
    target 4
    delay 29
    bw 63
  ]
  edge [
    source 3
    target 5
    delay 25
    bw 89
  ]
  edge [
    source 4
    target 5
    delay 34
    bw 111
  ]
]
