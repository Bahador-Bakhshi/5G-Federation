graph [
  node [
    id 0
    label 1
    disk 7
    cpu 1
    memory 10
  ]
  node [
    id 1
    label 2
    disk 6
    cpu 4
    memory 1
  ]
  node [
    id 2
    label 3
    disk 1
    cpu 1
    memory 11
  ]
  node [
    id 3
    label 4
    disk 3
    cpu 4
    memory 15
  ]
  node [
    id 4
    label 5
    disk 1
    cpu 2
    memory 6
  ]
  node [
    id 5
    label 6
    disk 8
    cpu 1
    memory 16
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 35
    bw 146
  ]
  edge [
    source 0
    target 1
    delay 26
    bw 150
  ]
  edge [
    source 0
    target 2
    delay 28
    bw 111
  ]
  edge [
    source 0
    target 3
    delay 26
    bw 138
  ]
  edge [
    source 1
    target 5
    delay 33
    bw 157
  ]
  edge [
    source 2
    target 5
    delay 27
    bw 97
  ]
  edge [
    source 3
    target 4
    delay 25
    bw 86
  ]
  edge [
    source 4
    target 5
    delay 28
    bw 169
  ]
]
