graph [
  node [
    id 0
    label 1
    disk 8
    cpu 2
    memory 13
  ]
  node [
    id 1
    label 2
    disk 3
    cpu 1
    memory 8
  ]
  node [
    id 2
    label 3
    disk 10
    cpu 3
    memory 6
  ]
  node [
    id 3
    label 4
    disk 7
    cpu 4
    memory 16
  ]
  node [
    id 4
    label 5
    disk 7
    cpu 2
    memory 14
  ]
  node [
    id 5
    label 6
    disk 1
    cpu 4
    memory 11
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 34
    bw 131
  ]
  edge [
    source 0
    target 1
    delay 28
    bw 72
  ]
  edge [
    source 1
    target 2
    delay 26
    bw 101
  ]
  edge [
    source 2
    target 3
    delay 33
    bw 153
  ]
  edge [
    source 2
    target 4
    delay 32
    bw 89
  ]
  edge [
    source 3
    target 5
    delay 27
    bw 145
  ]
  edge [
    source 4
    target 5
    delay 26
    bw 97
  ]
]
