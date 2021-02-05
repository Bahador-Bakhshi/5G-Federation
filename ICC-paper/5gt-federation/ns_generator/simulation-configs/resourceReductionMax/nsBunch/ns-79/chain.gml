graph [
  node [
    id 0
    label 1
    disk 1
    cpu 2
    memory 15
  ]
  node [
    id 1
    label 2
    disk 1
    cpu 3
    memory 7
  ]
  node [
    id 2
    label 3
    disk 10
    cpu 4
    memory 14
  ]
  node [
    id 3
    label 4
    disk 3
    cpu 3
    memory 3
  ]
  node [
    id 4
    label 5
    disk 5
    cpu 1
    memory 7
  ]
  node [
    id 5
    label 6
    disk 3
    cpu 1
    memory 8
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 34
    bw 162
  ]
  edge [
    source 0
    target 1
    delay 35
    bw 169
  ]
  edge [
    source 1
    target 2
    delay 31
    bw 140
  ]
  edge [
    source 1
    target 3
    delay 29
    bw 64
  ]
  edge [
    source 1
    target 4
    delay 31
    bw 150
  ]
  edge [
    source 2
    target 5
    delay 26
    bw 64
  ]
  edge [
    source 3
    target 5
    delay 25
    bw 117
  ]
  edge [
    source 4
    target 5
    delay 27
    bw 159
  ]
]
