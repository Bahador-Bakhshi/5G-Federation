graph [
  node [
    id 0
    label 1
    disk 6
    cpu 2
    memory 1
  ]
  node [
    id 1
    label 2
    disk 1
    cpu 2
    memory 15
  ]
  node [
    id 2
    label 3
    disk 1
    cpu 3
    memory 13
  ]
  node [
    id 3
    label 4
    disk 2
    cpu 1
    memory 13
  ]
  node [
    id 4
    label 5
    disk 1
    cpu 3
    memory 16
  ]
  node [
    id 5
    label 6
    disk 9
    cpu 4
    memory 9
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 30
    bw 123
  ]
  edge [
    source 0
    target 1
    delay 28
    bw 126
  ]
  edge [
    source 1
    target 2
    delay 32
    bw 130
  ]
  edge [
    source 1
    target 3
    delay 26
    bw 172
  ]
  edge [
    source 1
    target 4
    delay 32
    bw 127
  ]
  edge [
    source 2
    target 5
    delay 33
    bw 169
  ]
]
