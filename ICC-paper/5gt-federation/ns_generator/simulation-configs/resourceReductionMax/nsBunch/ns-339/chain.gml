graph [
  node [
    id 0
    label 1
    disk 2
    cpu 1
    memory 5
  ]
  node [
    id 1
    label 2
    disk 4
    cpu 2
    memory 9
  ]
  node [
    id 2
    label 3
    disk 2
    cpu 2
    memory 14
  ]
  node [
    id 3
    label 4
    disk 1
    cpu 1
    memory 13
  ]
  node [
    id 4
    label 5
    disk 9
    cpu 3
    memory 13
  ]
  node [
    id 5
    label 6
    disk 2
    cpu 2
    memory 4
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 25
    bw 91
  ]
  edge [
    source 0
    target 1
    delay 32
    bw 55
  ]
  edge [
    source 0
    target 2
    delay 26
    bw 182
  ]
  edge [
    source 0
    target 3
    delay 32
    bw 50
  ]
  edge [
    source 1
    target 4
    delay 26
    bw 175
  ]
  edge [
    source 2
    target 5
    delay 31
    bw 107
  ]
  edge [
    source 3
    target 5
    delay 35
    bw 191
  ]
  edge [
    source 4
    target 5
    delay 29
    bw 50
  ]
]
