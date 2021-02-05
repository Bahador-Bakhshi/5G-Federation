graph [
  node [
    id 0
    label 1
    disk 10
    cpu 1
    memory 12
  ]
  node [
    id 1
    label 2
    disk 3
    cpu 4
    memory 4
  ]
  node [
    id 2
    label 3
    disk 4
    cpu 1
    memory 4
  ]
  node [
    id 3
    label 4
    disk 10
    cpu 1
    memory 13
  ]
  node [
    id 4
    label 5
    disk 8
    cpu 2
    memory 12
  ]
  node [
    id 5
    label 6
    disk 9
    cpu 3
    memory 1
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 28
    bw 57
  ]
  edge [
    source 0
    target 1
    delay 34
    bw 89
  ]
  edge [
    source 1
    target 2
    delay 32
    bw 113
  ]
  edge [
    source 1
    target 3
    delay 30
    bw 111
  ]
  edge [
    source 2
    target 4
    delay 26
    bw 106
  ]
  edge [
    source 3
    target 4
    delay 26
    bw 159
  ]
  edge [
    source 4
    target 5
    delay 30
    bw 123
  ]
]
