graph [
  node [
    id 0
    label 1
    disk 5
    cpu 3
    memory 5
  ]
  node [
    id 1
    label 2
    disk 10
    cpu 4
    memory 9
  ]
  node [
    id 2
    label 3
    disk 7
    cpu 1
    memory 7
  ]
  node [
    id 3
    label 4
    disk 8
    cpu 2
    memory 8
  ]
  node [
    id 4
    label 5
    disk 10
    cpu 4
    memory 6
  ]
  node [
    id 5
    label 6
    disk 5
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
    delay 27
    bw 128
  ]
  edge [
    source 0
    target 1
    delay 32
    bw 179
  ]
  edge [
    source 0
    target 2
    delay 30
    bw 52
  ]
  edge [
    source 0
    target 3
    delay 31
    bw 188
  ]
  edge [
    source 1
    target 4
    delay 35
    bw 174
  ]
  edge [
    source 2
    target 4
    delay 28
    bw 176
  ]
  edge [
    source 3
    target 4
    delay 27
    bw 155
  ]
  edge [
    source 4
    target 5
    delay 31
    bw 165
  ]
]
