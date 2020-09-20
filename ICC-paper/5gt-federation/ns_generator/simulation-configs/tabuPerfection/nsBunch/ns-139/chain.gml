graph [
  node [
    id 0
    label 1
    disk 9
    cpu 2
    memory 7
  ]
  node [
    id 1
    label 2
    disk 2
    cpu 1
    memory 12
  ]
  node [
    id 2
    label 3
    disk 2
    cpu 1
    memory 13
  ]
  node [
    id 3
    label 4
    disk 10
    cpu 2
    memory 12
  ]
  node [
    id 4
    label 5
    disk 6
    cpu 2
    memory 12
  ]
  node [
    id 5
    label 6
    disk 8
    cpu 2
    memory 14
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 31
    bw 184
  ]
  edge [
    source 0
    target 1
    delay 26
    bw 114
  ]
  edge [
    source 0
    target 2
    delay 32
    bw 169
  ]
  edge [
    source 0
    target 3
    delay 33
    bw 146
  ]
  edge [
    source 1
    target 4
    delay 26
    bw 116
  ]
  edge [
    source 2
    target 4
    delay 29
    bw 192
  ]
  edge [
    source 3
    target 4
    delay 34
    bw 70
  ]
  edge [
    source 4
    target 5
    delay 31
    bw 86
  ]
]
